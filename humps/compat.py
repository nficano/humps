# -*- coding: utf-8 -*-
# flake8: noqa
import sys

PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3


def unicode(s):
    if PY2:
        return s.encode('utf-8')
    if PY3:
        return s
