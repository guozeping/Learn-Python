#!/usr/bin/env  python
# --*--coding:utf-8 --*--
from multiprocessing import Process
# -*- coding:utf-8 -*-
"""
pid=os.fork()
  1.只用在Unix系统中有效，Windows系统中无效
  2.fork函数调用一次，返回两次：在父进程中返回值为子进程id，在子进程中返回值为0
"""
# import os
# pid=os.fork()
# print(pid)
# if pid==0:
#   print("执行子进程，子进程pid={pid},父进程ppid={ppid}".format(pid=os.getpid(),ppid=os.getppid()))
# else:
#   print("执行父进程，子进程pid={pid},父进程ppid={ppid}".format(pid=pid,ppid=os.getpid()))
# from multiprocessing import Process
#
# nums = 10000
# def worker():
#    global nums
#    nums = nums - 1
#    print(nums)
#
# if __name__ == '__main__':
#     for i in range(1000):
#         process = Process(target=worker)
#         process.start()

from multiprocessing import Process
import os

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def f(name):
    info('function f')
    print('hello', name)

if __name__ == '__main__':
    info('main line')
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()