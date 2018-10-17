# -*- coding: utf-8 -*-
# flake8: noqa
import sys

_ver = sys.version_info
is_py2 = (_ver[0] == 2)
is_py3 = (_ver[0] == 3)


if is_py2:
    str = unicode


if is_py3:
    str = str
