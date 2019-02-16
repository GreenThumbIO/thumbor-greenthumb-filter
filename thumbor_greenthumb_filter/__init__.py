#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging

__version__ = '0.0.6'

try:
    from thumbor_greenthumb_filter.leaf_area import Filter  # NOQA
except ImportError:
    logging.exception('Could not import thumbor_greenthumb_filter.')
