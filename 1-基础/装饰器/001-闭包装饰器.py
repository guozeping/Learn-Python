# -*- coding: utf-8 -*-
# Created by Guozeping on 2019/6/19
import time

def decorator():
    def wrapper(*args,**kwargs):
        start_time = time.time()
        func()  # 调用下面的func()
        end_time = time.time()
        print(end_time-start_time)
    return wrapper

def func():
    time.sleep(0.8)


p = decorator()()

