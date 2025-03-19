#!/usr/bin/env python
# coding=utf-8
from __future__ import absolute_import, division, print_function

from .. import c

def test_c():
    assert c.do_something() == "|config|"
