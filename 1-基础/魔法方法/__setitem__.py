#!/usr/bin/env  python
# --*--coding:utf-8 --*--
class Foo:
    def __init__(self,name):
        self.name = name

    def __setitem__(self, key, value):
        print("key,value:",key,value)
        self.__dict__[key] = value

foo = Foo('gzp')
print(foo.__dict__)
foo['age'] = 26
print(foo.__dict__)