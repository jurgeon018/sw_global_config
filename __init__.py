from django.apps import AppConfig 

from django.utils.translation import gettext_lazy as _


class SiteSettingConfig(AppConfig):
    name = 'sw_global_config'
    verbose_name = _('Налаштування сайту')

default_app_config = 'sw_global_config.SiteSettingConfig'
