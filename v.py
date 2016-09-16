#!/usr/bin/env python
# coding=utf-8
from __future__ import absolute_import, division, print_function
import f
def do_something():
    return "|ssl connect|" + f.do_something()

print("V!")

if __name__ == "__main__":
    print("V main!")
    print(do_something())
