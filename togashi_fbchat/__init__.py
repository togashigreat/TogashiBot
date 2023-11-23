# -*- coding: UTF-8 -*-
"""Facebook Chat (Messenger) for Python

:copyright: (c) 2015 - 2019 by Taehoon Kim
:license: BSD 3-Clause, see LICENSE for more details.
"""
from __future__ import unicode_literals

# These imports are far too general, but they're needed for backwards compatbility.
from .models import *

from ._client import Client
from ._util import log  # TODO: Remove this (from examples too)
"""
the __message.py file was modified by Muhammad MuQiT and fixed some bugs. And some improper error handling
so, if you are using pip fbchat api, it won't work for TogashiBot
"""
__title__ = "fbchat"
__version__ = "1.9.7"
__description__ = "Facebook Chat (Messenger) for Python"

__copyright__ = "Copyright 2015 - 2019 by Taehoon Kim"
__license__ = "BSD 3-Clause"

__author__ = "Taehoon Kim; Moreels Pieter-Jan; Mads Marquart"
__email__ = "carpedm20@gmail.com"

__all__ = ["Client"]
