#!/usr/bin/env  python
# --*--coding:utf-8 --*--
class Foo(object):
    __slots__ = ['x','y']

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __getitem__(self, item):
        self.__dict__[item]

