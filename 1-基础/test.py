#!/usr/bin/env python
# coding=utf-8
class File(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)


