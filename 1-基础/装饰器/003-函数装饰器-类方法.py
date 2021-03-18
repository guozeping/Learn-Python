# -*- coding: utf-8 -*-
# Created by Guozeping on 2019/6/19
import time


def decorator(func):
    def wrapper(me_instance):
        start_time = time.time()
        func(me_instance)
        end_time = time.time()
        print(end_time - start_time)

    return wrapper


class Method(object):
    @decorator
    def func(self):
        time.sleep(0.8)


# 执行函数 仅表示执行
p1 = Method()
p1.func()  # 函数调用
