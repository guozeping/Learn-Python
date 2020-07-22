# -*- coding: utf-8 -*-
# Created by Guozeping on 2019/6/22
"""with 详解
1.上下文管理协议（Context Management Protocol）:包含方法__enter__()__exit(),支持该协议的
对象要实现这俩个方法。
2.上下文管理器（Context Manager）:支持上下文管理协议的对象,这种对象实现了__enter__()和__exit__()方法。
上下文管理器定义执行with语句时要建立的运行时上下文，负责执行with语句块上下文中的进入与退出操作。通常使用with语句条用上下文
管理器，也可以通过直接调用其他方法来使用。
3.运行时上下文（runtime context）：由上下文管理器创建，通过上下文管理器的__enter__()和__exit()__方法实现，__enter__()方法
在语句执行之前进入运行时上下文，__exit__()在语句体执行完之后从运行时上下文退出。with语句支持运行时上下文这一概念。
4-教程.上下文表达式（Context Expression）:with语句中跟关键字with之后的表达式，该表达式哟啊返回一个上下文管理器对象。
5.语句体（with-body）：with语句包裹起来的代码块，在执行语句之前会调用上下文管理器的__enter__()方法，执行完与具体之后会执行__exit__()
方法。

"""


