# -*- coding: utf-8 -*-
# Created by iFantastic on 2019/4-教程/16
'''
    在python类中没有真正的私有属性和方法，没有真正的私有化。
    _的属性和方法为私有方法或属性，提示该属性和方法不应在外部调用，也不会被
from ModuleA import * 导入。真调用了不会出错，但不符合规范
'''
# _的含义
class TestA:
    def _method(self):
        print("I am a private function")
    def method(self):
        return self._method()
ca = TestA()
ca.method()
"""
在类TestA中定义了一个_method方法，按照约定是不能在类外面直接调用它的，为了可以在外面使用_method方法，又定义了method方法，method方法调用_method方法。
但是我们应该记住的是加了_的方法也可以在类外面调用：
"""

# __的含义
class TestA:
    def __method(self):
        print("this is a method from class TestA")
    def method(self):
        return self.__method()
class TestB(TestA):
    def __method(self):
        print("this is a method from class TestB")

ca = TestA()
cb = TestB()
ca.method()
cb.method()