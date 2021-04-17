#!/usr/bin/env  python
# --*--coding:utf-8 --*--
class Test(object):
    def __init__(self):
        pass

    def __abs__(self,num):
        return abs(num)

test = Test()
test.b = -1
print(test.b)