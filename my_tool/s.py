#!/usr/bin/env python
# coding=utf-8
from __future__ import absolute_import, division, print_function
from . import t

def do_something():
    return t.do_something() + "|installed|"

print("S!")

def main():
    print("S main!")
    print(do_something())

if __name__ == "__main__":
    main()
