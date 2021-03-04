#!/usr/bin/env  python
# --*--coding:utf-8 --*--
"""
1.sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。

2.list 的 sort 方法返回的是对已经存在的列表进行操作，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。
"""
a = [5, 2, 3, 1, 4]
b = sorted(a)
print(a)
print(b)

a.sort()
print(a)