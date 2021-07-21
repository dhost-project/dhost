# Contributing

## Dev setup

To setup your dev env check the [docs/dev.md](./docs/dev.md).

## Style guide

* Single quotes are preffered (`'`), and double quotes for doc strings (`"""`).
* Use f-string format (`'{}'.format()` or `f'{}'`) instead of the %-format (`'%s' % ()`).

Some of the following tools are configured inside [setup.cfg](./setup.cfg).

### Editorconfig

There is also an [editorconfig]((https://editorconfig.org/)) file [.editorconfig](./.editorconfig) that can be used with your IDE or text editor.

* [VSCode extension](https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig)
* [Vim plugin](https://github.com/editorconfig/editorconfig-vim)
* [Emacs plugin](https://github.com/editorconfig/editorconfig-emacs)

### Black

[Black](https://github.com/psf/black) is a Python code formatter.

```bash
black .
```

### Flake8

[flake8](https://flake8.pycqa.org/en/latest/) is a Python code linter, it's used to verify coding errors and check style.

```bash
flake8 .
```

### isort

[isort](https://pycqa.github.io/isort/) is a Python utility / library to sort imports alphabetically, and automatically separated into sections and by type.

```bash
isort .
```

## Tools

### Pre-commit

[pre-commit](https://pre-commit.com/) is a git hook that will run before every commits. The pre-commit config can be found in [.pre-commit-config.yaml](./.pre-commit-config.yaml).

To install the pre-commit use:

```bash
pre-commit install
```

To test it use:

```bash
pre-commit run --all-file
```

### Tox

[tox](https://pypi.org/project/tox/) is a command line driven CI frontend and development task automation tool. It will launch multiple commands, format and lint the code and also run tests.

Run it with:

```bash
tox
```

## Translations

Create / update `.po` files.

```bash
django-admin makemessages -l fr -i=venv
```

You can translate the content located in the `/locale/<lang_code>/LC_MESSAGES/django.po` file.

Then compile `.po` to `.mo`.

```bash
django-admin compilemessages -i=venv
```

## Tests

If you add code don't forget to also write tests for it. For more informations about testing refer to the tests section from [docs/dev.md](./docs/dev.md).
