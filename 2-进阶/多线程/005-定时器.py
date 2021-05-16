#!/usr/bin/env  python
# --*--coding:utf-8 --*--
"""
原理比较简单，指定时间间隔后启动线程！适用场景：完成定时任务，例如：定时提醒-闹钟等等.
timer = threading.Timer(interval, function, args=None, kwargs=None)
"""
from threading import Timer


nums = 100000
def run():
    global nums
    nums = nums - 1
    print(nums)

if __name__ == '__main__':
    thread = Timer(5,run)
    thread.start()