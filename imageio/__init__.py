# -*- coding: utf-8 -*-
# Copyright (c) 2014-2020, imageio contributors
# imageio is distributed under the terms of the (new) BSD License.

# This docstring is used at the index of the documentation pages, and
# gets inserted into a slightly larger description (in setup.py) for
# the page on Pypi:
"""
Imageio is a Python library that provides an easy interface to read and
write a wide range of image data, including animated images, volumetric
data, and scientific formats. It is cross-platform, runs on Python 3.5+,
and is easy to install.

Main website: https://imageio.github.io
"""

# flake8: noqa

__version__ = "2.9.0"

# v3.0.0 API
from .core.imopen import imopen, _imopen

# Load some bits from core
from .core import FormatManager, RETURN_BYTES

# Instantiate format manager
formats = _imopen._legacy_format_manager

# Load legacy API
from .core.functions import (
    imread,
    mimread,
    volread,
    mvolread,
    imwrite,
    mimwrite,
    volwrite,
    mvolwrite,

    # aliases
    get_reader as read,
    get_writer as save,
    imwrite as imsave,
    mimwrite as mimsave,
    volwrite as volsave,
    mvolwrite as mvolsave,

    # misc
    help,
    get_reader,
    get_writer
)

from .core import functional_api as new_api

# Load all the plugins
from . import plugins

# expose the show method of formats
show_formats = formats.show

# Clean up some names
del FormatManager
