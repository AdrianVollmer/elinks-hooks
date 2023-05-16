import logging

log = logging.getLogger(__name__)


def safe_decompose(e):
    try:
        e.decompose()
    except AttributeError:
        # Happens with text
        pass


#  def follow_url_hook(url):
#      if 'www.heise.de' in url:
#          return url + '?view=print'
#      if 'www.npr.org' in url:
#          return url.replace('www.npr.org', 'text.npr.org')
#      if 'twitter.com' in url:
#          return url.replace('twitter.com', 'nitter.net')


#  def goto_url_hook(url):
#      if 'www.heise.de' in url:
#          return url + '?view=print'
#      if 'www.npr.org' in url:
#          return url.replace('www.npr.org', 'text.npr.org')


def load_hooks():
    """Load all YAML files in XDG_CONFIG_HOME"""
    import xdg.BaseDirectory
    from yaml import load, Loader
    import os

    path = xdg.BaseDirectory.save_config_path('elinks_hooks')
    hooks = {
        'pre_format_html': [],
        'follow_url': [],
        'goto_url': [],
        'quit': [],
        }

    files = [os.path.join(path, file)
             for file in os.listdir(path)
             if file.endswith('.yml')]

    for file in files:
        try:
            file = os.path.join(path, file)
            doc = open(file, 'r').read()
            yml = load(doc, Loader=Loader)
            for key in yml.keys():
                hooks[key].extend(yml[key])
        except Exception:
            log.error("Error loading file: %s" % file, exc_info=True)

    return hooks


class FormatActions(object):
    @staticmethod
    def remove(soup, selector=''):
        for e in soup.select(selector):
            e.decompose()

    # list items are always rendered on new-lines in ELinks...
    @staticmethod
    def to_span(soup, selector=''):
        e = soup.select(selector)
        span = soup.new_tag('span')
        span.contents = e.contents
        span.insert(0, soup.new_string(' • '))
        e.replaceWith(span)

    @staticmethod
    def add_border(soup, selector=''):
        for e in soup.select(selector):
            e['border'] = 1
            e['frame'] = 'box'

    @staticmethod
    def add_padding(soup, selector=''):
        for e in soup.select(selector):
            level = int(e['width']) // 40
            td = soup.new_tag('td')
            td['colspan'] = level
            td['border-left'] = 1
            e.parent.insert(0, td)

    @staticmethod
    def remove_socials(soup, selector=''):
        e = soup.select(selector)
        lists = e.select('ul')
        for each in lists:
            text = str(each).lower()
            count = 0
            for term in ['facebook', 'twitter', 'whatsapp', 'e-mail']:
                if term in text:
                    count += 1
            if count >= 2:
                each.decompose()

    @staticmethod
    def select(soup, selector=''):
        """Removes all elements except e and its parents"""
        e = soup.select(selector)
        body = soup.body
        for p in e.parents:
            if p and p.parent.name == 'body':
                soup.body.append(p)
                break
        for node in body.children:
            if p != node:
                safe_decompose(node)

    @staticmethod
    def replace_body(soup, selector=''):
        """Replace all children of <body> with this element"""
        e = soup.select(selector)
        body = soup.body
        body.clear()
        body.append(e)

    @staticmethod
    def delete_before(soup, selector=''):
        """Delete all previous sibling nodes"""
        for e in soup.select(selector):
            delete = []
            # Need to collect the nodes for deletion or else next_siblings
            # finishes early
            for node in e.previous_siblings:
                delete.append(node)
            for i, p in enumerate(e.parents):
                if p.name == 'body':
                    for node in delete:
                        safe_decompose(node)
                    return
                for node in p.previous_siblings:
                    delete.append(node)

    @staticmethod
    def delete_after(soup, selector=''):
        """Delete all following sibling nodes"""
        for e in soup.select(selector):
            delete = []
            # Need to collect the nodes for deletion or else next_siblings
            # finishes early
            for node in e.next_siblings:
                delete.append(node)
            for p in e.parents:
                if p.name == 'body':
                    for n in delete:
                        safe_decompose(n)
                    return
                for node in p.next_siblings:
                    delete.append(node)


class FollowActions(object):
    @staticmethod
    def add_parameter(url, key=None, value=None):
        import urllib.parse as urlparse
        from urllib.parse import urlencode
        url_parts = list(urlparse.urlparse(url))
        query = dict(urlparse.parse_qsl(url_parts[4]))
        query.update({key: value})
        url_parts[4] = urlencode(query)
        result = urlparse.urlunparse(url_parts)
        return result

    @staticmethod
    def replace(url, text=None, sub=None):
        return url.replace(text, sub)


class GotoActions(FollowActions):
    pass


class QuitActions(object):
    pass
