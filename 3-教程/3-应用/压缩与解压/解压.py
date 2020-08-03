# -*- coding:utf-8 -*-
# Created by Guozeping on 2019/10/2
import os
import glob
import zipfile

def unzip_file(dir_path):
    # 解压后文件存放的路径
    unzip_file_path = r"/Users/gzp/Desktop/解压文件"
    # 找到压缩文件夹
    dir_list = glob.glob(dir_path)
    if dir_list:
        # 循环zip文件夹
        for dir_zip in dir_list:
            # 以读的方式打开
            with zipfile.ZipFile(dir_zip, 'r') as f:
                for file in f.namelist():
                    f.extract(file,path=unzip_file_path)
            os.remove(dir_zip)
# 需要解压的文件路径
unzip_file(r"")