# -*- coding:utf-8 -*-
# Created by Guozeping on 2019/10/2
import xlwt

workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('My Sheet')

worksheet.write(0, 0, 5)
worksheet.write(0, 1, 2)
worksheet.write(1, 0, xlwt.Formula('A1*B1'))
worksheet.write(1, 1, xlwt.Formula('SUM(A1,B1)'))

workbook.save('Excel_workbook_2.xls')