#!/usr/bin/env  python
# --*--coding:utf-8 --*--
"""
is_set()
set()
clear()
wait()
"""
from threading import Thread
from threading import Timer

nums = 10000000

def run():
    global nums
    nums = nums - 1
    print(nums)

if __name__ == '__main__':
    pass