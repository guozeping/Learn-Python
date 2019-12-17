# -*- coding: utf-8 -*-
# Created by Guozeping on 2019/6/19
import time

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    @classmethod
    def now(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)
    def __str__(self):
        return '%s-%s-%s' % (self.year, self.month, self.day)
e = Date.now()
print(e)  # 2018-8-1


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    @staticmethod
    def now():
        t = time.localtime()
        return Date(t.tm_year, t.tm_mon, t.tm_mday)
    def __str__(self):
        return '%s-%s-%s' % (self.year, self.month, self.day)
e = Date.now()
print(e)  # 2018-8-1
