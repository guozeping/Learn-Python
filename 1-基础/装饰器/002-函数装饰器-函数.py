# -*- coding: utf-8 -*-
# Created by Guozeping on 2019/6/19
def outer(func):
    def inner(*args, **kwargs): pass

    return inner


@outer
def test(): pass

