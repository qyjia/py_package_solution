#!/usr/bin/env python
# coding=utf-8
from __future__ import absolute_import, division, print_function

import v


def test_v():
    assert v.do_something() == "|ssl connect||parse ASN.1|"
