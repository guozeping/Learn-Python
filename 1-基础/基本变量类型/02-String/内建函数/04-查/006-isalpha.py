#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'gzp'
"""
Return True if the string is an alphabetic string, False otherwise.

A string is alphabetic if all characters in the string are alphabetic and there
is at least one character in the string.        
"""
str_1 = "runoob"
str_2 = "runoob菜鸟教程"
str_3 = "Runoob example....wow!!!"
str_4 = "runoob123"

print(str_1.isalpha())  # true
print(str_2.isalpha())  # true
print(str_3.isalpha())  # false
print(str_4.isalpha())  # false
