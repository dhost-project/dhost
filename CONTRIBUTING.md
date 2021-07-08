# Contributing

## Dev setup

To setup your dev env check the [docs/dev.md](https://github.com/dhost-project/dhost/blob/master/docs/dev.md).

## Coding style

Some of the following tools are configured inside [setup.cfg](https://github.com/dhost-project/dhost/blob/master/setup.cfg).

### Editorconfig

There is also an [editorconfig]((https://editorconfig.org/)) file [.editorconfig](https://github.com/dhost-project/dhost/blob/master/.editorconfig) that can be used with your IDE or text editor.

* [VSCode extension](https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig)
* [Vim plugin](https://github.com/editorconfig/editorconfig-vim)
* [Emacs plugin](https://github.com/editorconfig/editorconfig-emacs)

### Yapf

[Yapf](https://pypi.org/project/yapf/) is a Python code formater.

```sh
yapf -i -r dhost
```

### Flake8

[flake8](https://flake8.pycqa.org/en/latest/) is a Python code linter, it's used to verify coding errors and check style.

```sh
flake8 dhost
```

### isort

[isort](https://pycqa.github.io/isort/) is a Python utility / library to sort imports alphabetically, and automatically separated into sections and by type.

```sh
isort .
```

### pydocstyle

[pydocstyle](https://pycodestyle.pycqa.org/en/latest/) is a tool to check your Python code against some of the style conventions in PEP 8.

```sh
pydocstyle dhost
```

## Tools

### Pre-commit

[pre-commit](https://pre-commit.com/) is a git hook that will run before every commits. The pre-commit config can be found in [.pre-commit-config.yaml](https://github.com/dhost-project/dhost/blob/master/.pre-commit-config.yaml).

To install the pre-commit use:

```sh
pre-commit install
```

To test it use:

```sh
pre-commit run --all-file
```

### Tox

[tox](https://pypi.org/project/tox/) is a command line driven CI frontend and development task automation tool. It will launch multiple commands, format and lint the code and also run tests.

Run it with:

```sh
tox
```

## Translations

Create / update `.po` files.

```sh
django-admin makemessages -l fr -i=venv
```

You can translate the content located in the `/locale/<lang_code>/LC_MESSAGES/django.po` file.

Then compile `.po` to `.mo`.

```sh
django-admin compilemessages -i=venv
```

## Tests

If you add code don't forget to also write tests for it. For more informations about testing refer to the tests section from [docs/dev.md](https://github.com/dhost-project/dhost/blob/master/docs/dev.md).
