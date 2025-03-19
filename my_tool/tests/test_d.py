#!/usr/bin/env python
# coding=utf-8
from __future__ import absolute_import, division, print_function

from .. import d


def test_d():
    assert d.do_something() == "|detected|"
