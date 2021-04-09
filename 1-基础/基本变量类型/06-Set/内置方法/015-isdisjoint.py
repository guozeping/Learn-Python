#!/usr/bin/env  python
# --*--coding:utf-8 --*--
"""
isdisjoint() 方法用于判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。。
"""
x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "facebook"}

z = x.isdisjoint(y)

print(z)