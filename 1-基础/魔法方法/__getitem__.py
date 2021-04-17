#!/usr/bin/env  python
# --*--coding:utf-8 --*--
class Foo:
    def __init__(self,name):
        self.name = name

    def __getitem__(self, item):
        print(self.__dict__[item])

foo = Foo('gzp')
print(foo.__dict__)
foo['name']