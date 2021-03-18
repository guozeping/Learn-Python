# -*- coding: utf-8 -*-
# Created by Guozeping on 2019/6/19
import time


# 1. 闭包
def decorator():
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func()  # 调用下面的func()
        end_time = time.time()
        print(end_time - start_time)

    return wrapper


def func():
    time.sleep(0.8)


p = decorator()()


# 2. 语法糖装饰器
def w1(fun):
    print('...装饰器开始装饰...')

    def inner():
        print('...验证权限...')
        fun()

    return inner


@w1  # 相当于 w1(test)
def test():
    print('test')


test()
