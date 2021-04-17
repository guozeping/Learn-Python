#!/usr/bin/env  python
# --*--coding:utf-8 --*--
class Person(object):
    def __init__(self,name):
        self.name = name

person = Person('gzp')
print(person.name)