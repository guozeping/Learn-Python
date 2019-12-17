# -*- coding: utf-8 -*-
# Created by Guozeping on 2019/6/19
class Foo:
    def __init__(self, name):
        self.__name = name
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('name must be str')
        self.__name = value
    @name.deleter
    def name(self):
        raise TypeError('can not delete')
f = Foo('jack')
print(f.name)  # jack
f.name = 'hanmeimei'
print(f.name)  # hanmeimei
# del f.name  # TypeError: can not delete

