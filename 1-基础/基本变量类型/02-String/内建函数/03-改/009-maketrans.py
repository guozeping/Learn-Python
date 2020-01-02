#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'gzp'
intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)

print(trantab)

str = "this is string example....wow!!!"
print (str.translate(trantab))