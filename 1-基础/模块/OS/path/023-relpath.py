#!/usr/bin/env  python
# --*--coding:utf-8 --*--
import os

path = '/Users/guozeping/Documents'
print(os.path.relpath(path,os.curdir))