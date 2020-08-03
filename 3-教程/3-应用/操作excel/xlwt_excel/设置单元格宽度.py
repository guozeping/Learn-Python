# -*- coding:utf-8 -*-
# Created by Guozeping on 2019/10/2
import xlwt
import datetime

workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('My Sheet')

style = xlwt.XFStyle()
style.num_format_str = 'M/D/YY'

worksheet.write(0,0,datetime.datetime.now(), style)
# 设置单元格宽度
worksheet.col(0).width = 3333
workbook.save('Excel_Workbook.xls')
