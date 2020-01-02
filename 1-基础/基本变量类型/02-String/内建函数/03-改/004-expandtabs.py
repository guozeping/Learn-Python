#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'gzp'
str = "this is\tstring example....wow!!!"

print("原始字符串: " + str)
print("替换 \\t 符号: " + str.expandtabs())
print("使用16个空格替换 \\t 符号: " + str.expandtabs(16))
