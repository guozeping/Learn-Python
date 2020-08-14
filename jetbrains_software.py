#!/usr/bin/env  python
# --*--coding:utf-8 --*--
import os

class fileprocesMixin():
    def newfolder(self):
        pass

    def filenamesplit(self):
        pass





class jetbrains_sortware(fileprocesMixin):
    def __init__(self,sourcepath, diremacpath,direubupath,direwinpath,softname):
        self.sourcepath = sourcepath
        self.diremacpath = diremacpath
        self.direubupath = direubupath
        self.direwinpath = direwinpath
        self.softname = softname


    @classmethod
    def allsourcefile(cls, sourfilepath):
        allfile = os.listdir(sourfilepath)
        print(allfile)


if __name__ == '__main__':
    sourfilepath = "/Users/guozeping/Downloads/"
    jetbrains_sortware.allsourcefile(sourfilepath)



