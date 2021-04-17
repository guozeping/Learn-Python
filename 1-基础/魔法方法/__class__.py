#!/usr/bin/env  python
# --*--coding:utf-8 --*--
class Person(object):
    def __init__(self,name):
        self.name = name


person = Person('gzp')
print(type(person))
print(person.__class__)
print(person.__class__.__class__)
print(person.__class__.__name__)