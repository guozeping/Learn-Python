#!/usr/bin/env  python
# --*--coding:utf-8 --*--
"""
symmetric_difference() 方法返回两个集合中不重复的元素集合，即会移除两个集合中都存在的元素。
"""
x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "apple"}

z = x.symmetric_difference(y)

print(z)