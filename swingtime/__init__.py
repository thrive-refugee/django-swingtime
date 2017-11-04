VERSION = (0, 8, 0)

def get_version():
    return '.'.join(map(str, VERSION))


default_app_config = 'swingtime.apps.SwingtimeAppConfig'
