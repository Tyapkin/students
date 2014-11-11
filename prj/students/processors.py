# -*- coding: utf-8 -*-


def settings_to_template_context(request):
    try:
        from django.conf import settings
        c = {'settings': settings}
    except ImportError:
        c = {'settings': None}

    return c
