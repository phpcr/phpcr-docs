This is the common Sphinx Theme for all Doctrine Project Documentations.

Use this by adding a submodule to your docs folder:

    git submodule add https://github.com/doctrine/doctrine-sphinx-theme.git en/_theme

Change the conf.py:

    html_theme = "doctrine"
    html_theme_path = ['_theme']
