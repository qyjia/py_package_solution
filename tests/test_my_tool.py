#!/usr/bin/env python
# coding=utf-8
from __future__ import absolute_import, division, print_function

import my_tool


def test_my_tool():
    assert my_tool.do_something() == "|main tool!||detected||tar edit!||installed||keys||LOL||ssl connect||parse ASN.1||config|"
