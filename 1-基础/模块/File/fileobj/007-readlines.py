#!/usr/bin/env  python
# --*--coding:utf-8 --*--
with open('../test.txt',errors='debug') as fp:
    lines = fp.readlines()
    print(lines)
