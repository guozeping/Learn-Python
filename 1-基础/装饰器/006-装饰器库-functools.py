# -*- coding: utf-8 -*-
# Created by Guozeping on 2019/6/19
def decorator(func):
    def inner_function():
        pass
    return inner_function

@decorator
def func():
    pass

print(func.__name__)

# 输出： inner_function

# 上述代码最后执行的结果不是 func，而是 inner_function！这表示被装饰函数自身的信息丢失了！怎么才能避免这种问题的发生呢？
#
# 可以借助functools.wraps()函数：
from functools import wraps
def decorator(func):
    @wraps(func)
    def inner_function():
        pass
    return inner_function

@decorator
def func():
    pass

print(func.__name__)

#输出： func
