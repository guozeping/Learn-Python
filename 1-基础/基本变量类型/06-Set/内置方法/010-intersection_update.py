#!/usr/bin/env  python
# --*--coding:utf-8 --*--
"""
intersection_update() 方法用于获取两个或更多集合中都重叠的元素，即计算交集。

intersection_update() 方法不同于 intersection() 方法，因为 intersection() 方法是返回一个新的集合，而 intersection_update() 方法是在原始的集合上移除不重叠的元素。
"""

x = {"apple", "banana", "cherry"}  # y 集合不包含 banana 和 cherry，被移除
y = {"google", "runoob", "apple"}

x.intersection_update(y)

print(x)


x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}

x.intersection_update(y, z)

print(x)