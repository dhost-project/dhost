# Django management commands

This a list of custom mangement commands available for the Dhost project.

To call a command use: `./manage.py <command>`.

| Command | Arguments | Description |
| --- | --- | --- |
| `cleartokens` | | Remove expired refresh tokens more infos [here](https://django-oauth-toolkit.readthedocs.io/en/latest/management_commands.html#cleartokens) |
| `generateavatar` | `<username>` | Generate an avatar for the user, this will remove the user's current avatar ! |
| `deltestdir` | `--noinput` | Delete the `TEST_DIR` folder and it's content |
