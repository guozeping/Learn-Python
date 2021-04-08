#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'gzp'
"""
python中 \t为4
"""
str = "runoob\t12345\tabc"

print(str)
print(str.expandtabs())
print(str.expandtabs(4))
print(str.expandtabs(8))
print(str.expandtabs(16))

