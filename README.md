Elinks Hooks
============

Kind of like Greasemonkey, but for elinks and in Python.


Installation
------------

```console
$ git clone https://github.com/AdrianVollmer/elinks-hooks.git
$ ln -s $(pwd)/elinks-hooks/elinks_hooks ~/.config/elinks/
$ echo 'from elinks_hooks import *  # noqa' > ~/.config/elinks/hooks.py
```

Note: elinks must be compiled with the Python scripting feature
(`./configure --with-python`). You can check with `elinks --version | grep Python`.


Rules
-----

Place rules in `$XDG_CONFIG_HOME/elinks_hooks/`. File names must end in
`.yml` and contain YAML. By default, `$XDG_CONFIG_HOME` is `~/.config`.


Why?
----

I read my RSS feeds in my terminal using
[newsboat](https://newsboat.org/index.html). Some feeds only show the
introduction instead of the full article, while other blogs frequently link
to news articles. Sometimes I also read [Hacker
News](https://news.ycombinator.com/) using newsboat, which clearly links to
lots of news articles and blogs linking to news articles.

When I want to read the full feed entry or news article, I use
[elinks](http://elinks.or.cz/) to quickly open the page. Since the sites are
optimized to be read with a full GUI browser, one sees lots of superflous
HTML elements. This collection of scripts allows me to display just the meat
of the article, or redirect twitter URLs to Nitter, etc.

As a side effect, pretty much all ads and other distractions are filtered.

License
-------

Copyright Adrian Vollmer, 2023. MIT Licensed.
