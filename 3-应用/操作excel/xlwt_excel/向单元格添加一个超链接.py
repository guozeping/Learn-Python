# -*- coding:utf-8 -*-
# Created by Guozeping on 2019/10/2
import xlwt

workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('My Sheet')

worksheet.write(0, 0, xlwt.Formula('HYPERLINK("http://www.baidu.com";"baidu")'))

workbook.save('Excel_Workbook_3.xls')