#!/usr/bin/env python
# coding=utf-8
from __future__ import absolute_import, division, print_function

import c
import d
import k
import s

print("my_tool!")
def do_something():
    return "|main tool!|" + d.do_something() + s.do_something() + k.do_something() + c.do_something()


if __name__ == "__main__":
    print("my_tool main!")
    print(do_something())
