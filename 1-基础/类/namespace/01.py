# -*- coding:utf-8 -*-
# Created by Guozeping on 2019/10/2
print('1.globas:',globals())
a = 100000000
def func():
    print('1.func locals:', locals())
    a = 1
    b = 2
    global p
    p = 9999

    def inner_func():
        print('1.inner_func locals:', locals())
        m = 3
        n = 4
        nonlocal a
        a = m + n
        print(a)
        print('2.inner_func locals:', locals())

    inner_func()
    print(a,b,p)
    print('2.func locals:', locals())

func()