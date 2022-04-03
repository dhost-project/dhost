import os


def env(var, default=None):
    return os.environ.get(var, default)


def env_list(var, default=None, separator=","):
    text_list = env(var, default)
    return [item.strip() for item in text_list.split(separator)]


def env_int(var, default=None):
    value = env(var, default)
    return int(value) if value else None


def env_float(var, default=None):
    value = env(var, default)
    return float(value) if value else None


def env_bool(var, default=None, trues=["True", "true", "1"]):
    return env(var, str(default)) in trues
