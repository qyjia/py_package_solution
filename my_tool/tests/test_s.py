#!/usr/bin/env python
# coding=utf-8
from __future__ import absolute_import, division, print_function

from .. import s


def test_my_tool():
    assert s.do_something() == "|tar edit!||installed|"
