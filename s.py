#!/usr/bin/env python
# coding=utf-8
from __future__ import absolute_import, division, print_function
import t
def do_something():
    return t.do_something() + "|installed|"

print("S!")

if __name__ == "__main__":
    print("S main!")
    print(do_something())

