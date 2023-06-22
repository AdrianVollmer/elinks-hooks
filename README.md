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
