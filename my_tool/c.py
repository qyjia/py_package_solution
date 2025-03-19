#!/usr/bin/env python
# coding=utf-8
from __future__ import absolute_import, division, print_function

def do_something():
    return "|config|"

print("C!")

def main():
    print("C main!")
    print(do_something())

if __name__ == "__main__":
    main()
