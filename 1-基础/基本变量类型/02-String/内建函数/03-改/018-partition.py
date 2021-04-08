#!/usr/bin/env  python
# --*--coding:utf-8 --*--
"""
返回一个3元的元组，第一个为分隔符左边的子串，第二个为分隔符本身，第三个为分隔符右边的子串。
"""
str = 'www.runoob.com'
print(str.partition("."))

rstr = str.rpartition(".")
print(rstr)

