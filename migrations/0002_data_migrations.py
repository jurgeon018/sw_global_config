from django.db import migrations
from sw_global_config.models import GlobalConfig
from sw_global_config import settings as sw_global_config_settings
from django.conf import settings


def migrate_settings(apps, schema_editor):
    global_config = GlobalConfig.get_solo()
    global_config.robots = sw_global_config_settings.META_ROBOTS
    global_config.favicon = sw_global_config_settings.FAVICON
    global_config.og_image_square = sw_global_config_settings.OGIMAGE_SQUARE
    global_config.og_image_rectangle = sw_global_config_settings.OGIMAGE_RECTANGLE
    global_config.host = settings.EMAIL_HOST
    global_config.port = settings.EMAIL_PORT
    global_config.from_email = settings.DEFAULT_FROM_EMAIL
    global_config.username = settings.EMAIL_HOST_USER
    global_config.password = settings.EMAIL_HOST_PASSWORD
    global_config.use_tls = settings.EMAIL_USE_TLS
    global_config.use_ssl = settings.EMAIL_USE_SSL
    global_config.save()


class Migration(migrations.Migration):

    dependencies = [
        ('sw_global_config', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(migrate_settings),
    ]
