# -*- coding: utf-8 -*-
# Created by Guozeping on 2019/6/19
def makebold(f):
    return lambda: '<b>' + f() + '</b>'

def makeitalic(f):
    return lambda: '<i>' + f() + '</i>'

@makebold
@makeitalic
def say():
    return 'hello'

a = say()
print(a)

