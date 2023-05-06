Elinks Hooks
============

Kind of like Greasemonkey, but for elinks and in Python.


Installation
------------

```console
$ pip install -e .
$ echo 'from elinks_hooks import *  # noqa' > ~/.config/elinks/hooks.py
```

If pip complains about externally managed environments, supply the
`--break-system-packages`. It will most likely not break anything, and
the suggested solution (virtual environments) won't work for this usecase.
Just don't be root.

Note: elinks must be compiled with the Python scripting feature
(`./configure --with-python`). You can check with `elinks --version | grep Python`.

Rules
-----

Place rules in `$XDG_CONFIG_HOME/elinks_hooks/`. File names must end in
`.yml` and contain YAML. By default, `$XDG_CONFIG_HOME` is `~/.config`.
