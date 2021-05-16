#!/usr/bin/env  python
# --*--coding:utf-8 --*--
from threading import Thread

nums = 100000000
def run1():
    for i in range(10000000):
        global nums
        nums = nums - 1
        print("nums1:-----", nums)

def run2():
    for i in range(10000000):
        global nums
        nums = nums - 1
        print("nums2:-----", nums)

if __name__ == '__main__':
    thread1 = Thread(target=run1)
    thread2 = Thread(target=run2)
    thread1.start()
    thread2.start()
