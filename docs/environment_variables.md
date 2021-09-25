# Environment variables

This document detail the env variables that you can/must set for the DHost app.

## DJANGO_ENV

The variable `DJANGO_ENV` define wich environment to use. By default it's `development`, and can be set to `production` or `tests`.

## Legend

| Emojie | Meaning                                                                                   |
| ------ | ----------------------------------------------------------------------------------------- |
| ✅     | You must change this value for the website to work in production.                         |
| ❓     | Heavly dependant on your infrastructure, you should look at this option.                  |
| 🍪     | You should set this variable but it won't break the site if you don't.                    |
| 🤷     | It's up to you if you want to set the value in most cases this will enable site features. |
| ❌     | You shouldn't change this value.                                                          |

## Variables

Note:

* `ROOT_DIR` is the location of the base directory wich is the root project's folder.
* `BASE_DIR` is at `ROOT_DIR/dhost`, it's the apps root.

| Environment variables            | Prod | Default values             | Descriptions                                                                                                                                                                |
| ---------------------------      | :--: | :---------------------:    | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `DEBUG`                          | ✅   | `True`                     | Set to `False` for production, more infos [here](https://docs.djangoproject.com/en/3.1/ref/settings/#debug).                                                                |
| `DJANGO_SECRET_KEY`              | ✅   |                            | Your website secret key, more infos [here](https://docs.djangoproject.com/en/3.1/ref/settings/#secret-key).                                                                 |
| `SITE_ID`                        | ❓   | `1`                        | More infos [here](https://docs.djangoproject.com/en/3.1/ref/settings/#site-id).                                                                                             |
| `ALLOWED_HOSTS`                  | ✅   | `localhost,127.0.0.1`      | A list of strings representing the host/domain names that this Django site can serve. More infos [here](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts). |
| `CORS_ALLOWED_ORIGINS`           | ✅   | `http://localhost:8000`    | A list of strings representing the CORS allowed hosts. More infos [here](https://github.com/adamchainz/django-cors-headers).                                                |
| `CORS_ALLOW_ALL_ORIGINS`         | ❌   | _DEBUG_                    | Set allowed hosts to `*`, by default it take the value of `DEBUG`.                                                                                                          |
| `ENABLE_SSL`                     | ❌   | `1`                        | Enable all SSL (redirect, cookie), enabled by default in production only.                                                                                                   |
| `DATABASE_URL`                   | 🍪   | `sqlite:///db.sqlite3`     | The database URL, more infos [here](https://github.com/jacobian/dj-database-url#url-schema).                                                                                |
| `REDIS_URL`                      | 🍪   |                            | The URL to the Redis server.                                                                                                                                                |
| `SENTRY_DSN`                     | 🍪   |                            | The Sentry DSN URL, more infos [here](https://sentry.io/welcome/).                                                                                                          |
| `EMAIL_HOST`                     | 🍪   | `localhost`                | The host to use for sending email. More infos [here](https://docs.djangoproject.com/en/3.1/ref/settings/#email-host).                                                       |
| `SERVER_EMAIL`                   | 🍪   | `root@localhost`           | More infos [here](https://docs.djangoproject.com/en/3.1/ref/settings/#server-email).                                                                                        |
| `DEFAULT_FROM_EMAIL`             | 🍪   | `webmaster@localhost`      | More infos [here](https://docs.djangoproject.com/en/3.1/ref/settings/#default-from-email).                                                                                  |
| `EMAIL_PORT`                     | 🍪   | `1025`                     | More infos [here](https://docs.djangoproject.com/en/3.1/ref/settings/#email-port).                                                                                          |
| `CSRF_COOKIE_SECURE`             | 🍪   | `False`                    | Whether to use a secure cookie for the CSRF cookie. More infos [here](https://docs.djangoproject.com/en/3.1/ref/settings/#csrf-cookie-secure).                              |
| `SESSION_COOKIE_SECURE`          | 🍪   | `False`                    | Whether to use a secure cookie for the session cookie. More infos [here](https://docs.djangoproject.com/en/3.1/ref/settings/#session-cookie-secure).                        |
| `STATIC_URL`                     | 🍪   | `/static/`                 | URL to use when referring to static files. More infos [here](https://docs.djangoproject.com/en/3.1/ref/settings/#static-url).                                               |
| `STATIC_ROOT`                    | ❓   | `BASE_DIR / 'static'`      | The absolute path to the directory where collectstatic will collect static files. More infos [here](https://docs.djangoproject.com/en/3.1/ref/settings/#static-root).       |
| `MEDIA_URL`                      | 🍪   | `/media/`                  | URL that handles the media served. More infos [here](https://docs.djangoproject.com/en/3.1/ref/settings/#media-url).                                                        |
| `MEDIA_ROOT`                     | ❌   | `BASE_DIR / 'media'`       | Absolute filesystem path to the directory that will hold user-uploaded files. More infos [here](https://docs.djangoproject.com/en/3.1/ref/settings/#media-root).            |
| `SOCIAL_AUTH_GITHUB_KEY`         | ✅   |                            | Github OAuth2 client ID.                                                                                                                                                    |
| `SOCIAL_AUTH_GITHUB_SECRET`      | ✅   |                            | Github OAuth2 client secret.                                                                                                                                                |
| `DJANGO_DEFAULT_FILE_STORAGE`    | ❓   | `default`                  | Wich default file storage to use, one of `default`, `aws`, `google`.                                                                                                        |
| `DJANGO_STATICFILES_STORAGE`     | ❓   | `whitenoise`               | Wich staticfiles storage to be used, one of `whitenoise`, `aws`, `google`.                                                                                                  |
| `GITHUB_REPOS_ROOT`              | ❓   | `MEDIA_ROOT / 'github'`    | Absolute filesystem path to the directory that will hold Github repos files.                                                                                                |
| `CELERY_BROKER_URL`              | ❓   | `redis://127.0.0.1:6379/0` | Celery broker URL.                                                                                                                                                          |
| `CELERY_RESULT_BACKEND`          | ❓   | `redis://127.0.0.1:6379/0` | Celery broker URL.                                                                                                                                                          |
| `AWS_ACCESS_KEY_ID`              | ❓   |                            | AWS access key more infos [here](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html).                                                                 |
| `AWS_SECRET_ACCESS_KEY`          | ❓   |                            | AWS secret key.                                                                                                                                                             |
| `AWS_DEFAULT_ACL`                | ❓   | `None`                     | AWS ACL.                                                                                                                                                                    |
| `AWS_STORAGE_BUCKET_NAME`        | ❓   |                            | AWS bucket name, giving a storage bucket name will enable storage of staticfiles.                                                                                           |
| `AWS_S3_CUSTOM_DOMAIN`           | ❓   |                            | Custom domain for static bucket.                                                                                                                                            |
| `AWS_MEDIA_BUCKET_NAME`          | ❓   |                            | AWS bucket name, giving a media bucket name will enable storage of media files.                                                                                             |
| `AWS_MEDIA_CUSTOM_DOMAIN`        | ❓   |                            | Custom domain for media bucket.                                                                                                                                             |
| `STATIC_URL`                     | ❓   | `/static/`                 | For AWS: `https://<bucket_name>.s3.amazonaws.com/<static>/`.                                                                                                                |
| `AWS_LOCATION`                   | ❓   |                            | The base path inside you S3 bucket.                                                                                                                                         |
| `AWS_S3_REGION_NAME`             | ❓   |                            | AWS region name.                                                                                                                                                            |
| `GOOGLE_APPLICATION_CREDENTIALS` | ❓   |                            |                                                                                                                                                                             |
| `GS_BUCKET_NAME`                 | ❓   |                            |                                                                                                                                                                             |
| `GS_PROJECT_ID`                  | ❓   |                            |                                                                                                                                                                             |
| `GS_DEFAULT_ACL`                 | ❓   |                            |                                                                                                                                                                             |
| `GS_QUERYSTRING_AUTH`            | ❓   |                            |                                                                                                                                                                             |
| `GS_LOCATION`                    | ❓   |                            |                                                                                                                                                                             |
| `GS_MEDIA_BUCKET_NAME`           | ❓   |                            |                                                                                                                                                                             |
