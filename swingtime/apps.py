from django.apps import AppConfig

class SwingtimeAppConfig(AppConfig):
    name = 'swingtime'
    _zero_width_space = '\u200B'  # used to make it last alphabetically, better option: http://stackoverflow.com/questions/398163/ordering-admin-modeladmin-objects-in-django-admin
    verbose_name = _zero_width_space + 'Calendar Configuration'
