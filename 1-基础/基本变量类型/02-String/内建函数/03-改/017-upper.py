#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'gzp'
"""
Return a copy of the string with all the cased characters 4 converted to uppercase. 
Note that s.upper().isupper() might be False if s contains uncased characters or if 
the Unicode category of the resulting character(s) is not “Lu” (Letter, uppercase), but e.g. “Lt” (Letter, titlecase).

The uppercasing algorithm used is described in section 3.13 of the Unicode Standard.
"""
str = "This is string example from runoob....wow!!!";
str_copy = str.upper()

print(str)
print(str_copy)