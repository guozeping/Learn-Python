#!/usr/bin/env  python
# --*--coding:utf-8 --*--
from threading import Thread

nums = 100000000000000
def run():
    for i in range(100000000):
        global nums
        nums = nums - 1
        print(nums)


if __name__ == '__main__':
    thread = Thread(target=run)
    thread.setDaemon(True)
    thread.start()
