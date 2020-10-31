from sw_global_config.models import *


def context(request):
    global_config   = GlobalConfig.get_solo()
    return locals()


