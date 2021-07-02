# Contributing

## Dev setup

To setup your dev env check the [docs/dev.md](docs/dev.md).

## Coding style

Some of the following tools are configured inside [setup.cfg](setup.cfg).

### Pre-commit

[pre-commit](https://pre-commit.com/) is a git hook that will run before every commits. The pre-commit config can be found in [.pre-commit-config.yaml](.pre-commit-config.yaml).

To install the pre-commit use:

```sh
pre-commit install
```

To test it use:

```sh
pre-commit run --all-file
```

### Editorconfig

There is also an [editorconfig]((https://editorconfig.org/)) file [.editorconfig](.editorconfig) that can be used with your IDE or text editor.

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

## Links

* [Django doc](https://docs.djangoproject.com/en/3.2/)
* [Django REST doc](https://www.django-rest-framework.org/)
