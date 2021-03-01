# Environment variables

This document detail the env variables that you can/must set for the DHost app.

## Legend

| Emojie | Meaning |
| --- | --- |
| ✅ | You must change this value for the website to work in production. |
| ❓ | Heavly dependant on your infrastructure, you should look at this option. |
| 🍪 | You should set this variable but it won't break the site if you don't. |
| 🤷 | It's up to you if you want to set the value in most cases this will enable site features. |
| ❌ | You shouldn't change this value. |

## Variables

Note:
- `BASE_DIR` is the location of the base directory wich is the root project's folder.

| Environment variables | Prod | Default values | Descriptions |
| --- | --- | --- | --- |
| `DEBUG` | ✅ | `True` | Set to `False` for production, more infos [here](https://docs.djangoproject.com/en/3.1/ref/settings/#debug). |
| `SECRET_KEY` | ✅ | *auto generated* | Your website secret key, more infos [here](https://docs.djangoproject.com/en/3.1/ref/settings/#secret-key) |
| `SITE_ID` | ❓ | `1` | More infos [here](https://docs.djangoproject.com/en/3.1/ref/settings/#site-id). |
| `ALLOWED_HOSTS` | ✅ | `localhost,127.0.0.1` | A list of strings representing the host/domain names that this Django site can serve. More infos [here](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts). |
| `DATABASE_URL` | 🍪 | `sqlite:///db.sqlite3` | The database URL, more infos [here](https://github.com/jacobian/dj-database-url#url-schema). |
| `REDIS_URL` | 🍪 | | The URL to the Redis server. |
| `SENTRY_DSN` | 🍪 | | The Sentry DSN URL, more infos [here](https://sentry.io/welcome/). |
| `EMAIL_HOST` | 🍪 | `localhost` | The host to use for sending email. More infos [here](https://docs.djangoproject.com/en/3.1/ref/settings/#email-host). |
| `SERVER_EMAIL` | 🍪 | `root@localhost` | More infos [here](https://docs.djangoproject.com/en/3.1/ref/settings/#server-email). |
| `DEFAULT_FROM_EMAIL` | 🍪 | `webmaster@localhost` | More infos [here](https://docs.djangoproject.com/en/3.1/ref/settings/#default-from-email). |
| `EMAIL_PORT` | 🍪 | `1025` | More infos [here](https://docs.djangoproject.com/en/3.1/ref/settings/#email-port). |
| `CSRF_COOKIE_SECURE` | 🍪 | `False` | Whether to use a secure cookie for the CSRF cookie. More infos [here](https://docs.djangoproject.com/en/3.1/ref/settings/#csrf-cookie-secure). |
| `SESSION_COOKIE_SECURE` | 🍪 | `False` | Whether to use a secure cookie for the session cookie. More infos [here](https://docs.djangoproject.com/en/3.1/ref/settings/#session-cookie-secure). |
| `DEBUG_TOOLBAR` | ❌ | `False` | Activate or not the Django debug toolbar, more infos [here](https://django-debug-toolbar.readthedocs.io/en/latest/). |
| `STATIC_URL` | 🍪 | `/static/` | URL to use when referring to static files. More infos [here](https://docs.djangoproject.com/en/3.1/ref/settings/#static-url) |
| `STATIC_ROOT` | ❓ | `BASE_DIR / 'static'` | The absolute path to the directory where collectstatic will collect static files. More infos [here](https://docs.djangoproject.com/en/3.1/ref/settings/#static-root). |
| `MEDIA_URL` | 🍪 | `/media/` | URL that handles the media served. More infos [here](https://docs.djangoproject.com/en/3.1/ref/settings/#media-url). |
| `MEDIA_ROOT` | ❌ | `BASE_DIR / 'media'` | Absolute filesystem path to the directory that will hold user-uploaded files. More infos [here](https://docs.djangoproject.com/en/3.1/ref/settings/#media-root). |
| `SOCIAL_AUTH_GITHUB_KEY` | ✅ | | Github OAuth2 client ID |
| `SOCIAL_AUTH_GITHUB_SECRET` | ✅ | | Github OAuth2 client secret |
| `DRFSO2_PROPRIETARY_BACKEND_NAME` | 🤷 | `Dhost` | |
| `ENABLE_RECAPTCHA` | 🤷 | `False` | Enable the reCAPTCHA on forms. |
| `RECAPTCHA_PUBLIC_KEY` | 🤷 | *dev key* | You need to create a Google reCAPTCHA V3 account [here](https://www.google.com/recaptcha/intro/index.html) to get the key. See [here](https://github.com/praekelt/django-recaptcha#installation) for more details. |
| `RECAPTCHA_PRIVATE_KEY` | 🤷 | *dev key* | Same has for `RECAPTCHA_PUBLIC_KEY`. |