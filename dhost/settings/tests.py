from .defaults import *  # noqa

SECRET_KEY = "only_a_test_key"

# faster password hashing for tests
PASSWORD_HASHERS = ("django.contrib.auth.hashers.MD5PasswordHasher",)

# disable logging during tests
LOGGING = {}
