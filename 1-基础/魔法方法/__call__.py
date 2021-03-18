#!/usr/bin/env  python
# --*--coding:utf-8 --*--
class Test(object):
    def __init__(self, name):
        self.name = name

    def __call__(self, *args, **kwargs):
        return self.name

test = Test("gzp")
print(test())
