#!/usr/bin/env python
# coding=utf-8
from __future__ import absolute_import, division, print_function

from . import v

def do_something():
    data = ""
    with open("resources/lol.txt") as f:
        data = f.read().strip()
    return "|keys|" + data + v.do_something()

print("K!")

def main():
    print("K main!")
    print(do_something())

if __name__ == "__main__":
    main()
