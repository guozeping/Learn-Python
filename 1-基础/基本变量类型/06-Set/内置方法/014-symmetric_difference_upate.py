#!/usr/bin/env  python
# --*--coding:utf-8 --*--
"""
symmetric_difference_update() 方法移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中。
"""
x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "apple"}

x.symmetric_difference_update(y)

print(x)