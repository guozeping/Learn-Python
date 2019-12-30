#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 2019/4/16
'''
global 修改全局变量
nonlocal_global 修改嵌套函数作用域变量
'''

name = 'pythontab'
def func():
    global name
    name = 'pythontab.com'
func()
print(name)


def func():
    name = 'pythontab'
    def foo():
        nonlocal name
        name = 'pythontab.com'
    foo()
    print(name)
func()


