def get_envvars_dict(envvars):
    # Generate dict of the environment variables
    envvars_dict = {}
    for var_object in envvars:
        envvars_dict[var_object.variable] = var_object.value
    return envvars_dict
