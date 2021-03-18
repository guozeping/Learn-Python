# -*- coding: utf-8 -*-
# Created by Guozeping on 2019/6/19
#################  类装饰器  #################
class Decorator(object):
    def __init__(self, f):
        self.f = f

    # __call__ 是一个特殊的方法，可将一个类实例变成一个可调用对象，
    def __call__(self, *args, **kwargs):
        print('decorator start')
        self.f()  # 此处是f()
        print('decorator end')


@Decorator
def func():
    print('func')


func()


#################  破解版  #################
class Decorator(object):
    def __init__(self, f):
        self.f = f

    # __call__ 是一个特殊的方法，可将一个类实例变成一个可调用对象，
    def __call__(self, *args, **kwargs):
        print('decorator start')
        self.f()  # 此处是f()
        print('decorator end')


def func():
    print('func')


p = Decorator(func)
p()
