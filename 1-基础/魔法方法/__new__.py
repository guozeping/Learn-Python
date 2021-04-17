#!/usr/bin/env  python
# --*--coding:utf-8 --*--
class Person(object):
    def __init__(self,name):
        self.name = name
        print(self)
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)

person = Person("gzp")
print(person)