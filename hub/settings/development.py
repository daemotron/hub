# -*- coding: utf-8 -*-
"""
    development
    ~~~~~~~~~~~~~~~~~~~~~~

    :copyright: Copyright 2016 by The Stormrose Project team, see AUTHORS.
    :license: MIT License, see LICENSE for details.
"""

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATES[0]['OPTIONS'].update({'debug': True})

# Show emails to console in DEBUG mode
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
