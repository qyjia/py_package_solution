#!/usr/bin/env python
# coding=utf-8
from __future__ import absolute_import, division, print_function
from . import f

def do_something():
    return "|ssl connect|" + f.do_something()

print("V!")

def main():
    print("V main!")
    print(do_something())

if __name__ == "__main__":
    main()
