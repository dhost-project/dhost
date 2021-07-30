import hashlib


def gravatar_hash(email):
    return hashlib.md5(email.lower().encode("utf-8")).hexdigest()
