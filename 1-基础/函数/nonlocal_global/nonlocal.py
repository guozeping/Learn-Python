# -*- coding: utf-8 -*-
# Created by Guozeping on 2019/6/19

# 当前作用域局部变量->外层作用域变量->当前模块中的全局变量->python内置变量。
# 而python中unlocal的作用为变当前作用域局部变量为最临近外层（非全局）作用域变量。
# 而global的作用为变当前作用域局部变量为当前模块中的全局变量。

# def test_nonlocal():
#     dd = 0
#     def test2():
#         dd += 2  # 此处错
#     test2()
#     print(dd)
# test_nonlocal()

def test_nonlocal():
    dd = 0
    def test2():
        nonlocal dd
        dd += 2
    test2()
    print(dd)
test_nonlocal()

# 列2
"""
1.

"""
def test_nonlocal():
    dd = 0
    def test2():
        def test3():
            dd = 3
            def test4():
                nonlocal dd
                dd += 2
                print(dd)
            test4()
        test3()
    test2()
    print(dd)
test_nonlocal()
"""
执行结果
    5
    0
"""

#