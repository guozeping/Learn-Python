# -*- coding: utf-8 -*-
# Created by Guozeping on 2019/6/19
"""
当python解释器执行到这句话的时候，会去调用w1函数，同时将被装饰的函数名作为参数传入(此时为f1)，
根据闭包一文分析，在执行w1函数的时候，此时直接把inner函数返回了，同时把它赋值给f1，
此时的f1已经不是未加装饰时的f1了，而是指向了w1.inner函数地址。
"""
# import time
#
# def decorator():
#     def wrapper(*args,**kwargs):
#         start_time = time.time()
#         func()  # 调用下面的func()
#         end_time = time.time()
#         print(end_time-start_time)
#     return wrapper
#
# def func():
#     time.sleep(0.8)
#
#
# p = decorator()()

"""装饰器原理"""
# 1、
def w1(fun):
    print('...装饰器开始装饰...')
    def inner():
        print('...验证权限...')
        fun()
    return inner

@w1  # 解释器执行到这儿的时候会装饰 并把inner函数名赋值给test
def test():
    print('test')

# 2、
def w1(fun):
    print('...装饰器开始装饰...')
    def inner():
        print('...验证权限...')
        fun()
    return inner

@w1  # 解释器执行到这儿的时候会装饰 并把inner函数名赋值给test
def test():
    print('test')

test()