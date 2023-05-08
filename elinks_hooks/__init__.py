import re
import logging

from bs4 import BeautifulSoup

from elinks_hooks.log import init_logger
from elinks_hooks.rules import load_hooks, FormatActions, FollowActions, \
        GotoActions, QuitActions

init_logger()
log = logging.getLogger(__name__)
hooks = load_hooks()


def pre_format_html_hook(url, html):
    soup = None

    for h in hooks['pre_format_html']:
        if re.search(h['url'], url):
            if not h['actions']:
                continue

            log.info("Applying %d pre_format_html actions to %s..."
                     % (len(h['actions']), url))

            for a in h['actions']:
                if soup is None:
                    # Parse html only if necessary
                    soup = BeautifulSoup(html, 'lxml')
                modifier = getattr(FormatActions, a['name'])
                modifier(soup, **a['args'])

    if soup is not None:
        return str(soup)


def follow_url_hook(url):
    for h in hooks['follow_url']:
        if re.match(h['url'], url):
            modifier = getattr(FollowActions, h['name'])
            return modifier(**h['args'])


def goto_url_hook(url):
    for h in hooks['goto_url']:
        if re.match(h['url'], url):
            modifier = getattr(GotoActions, h['name'])
            return modifier(**h['args'])


def quit_hook():
    for h in hooks['quit']:
        modifier = getattr(QuitActions, h['name'])
        return modifier(**h['args'])
