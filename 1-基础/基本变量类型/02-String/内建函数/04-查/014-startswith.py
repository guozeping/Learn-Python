#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'gzp'
str = "this is string example....wow!!!"
print (str.startswith( 'this' ))   # 字符串是否以 this 开头
print (str.startswith( 'string', 8 ))  # 从第八个字符开始的字符串是否以 string 开头
print (str.startswith( 'this', 2, 4 )) # 从第2个字符开始到第四个字符结束的字符串是否以 this 开头
