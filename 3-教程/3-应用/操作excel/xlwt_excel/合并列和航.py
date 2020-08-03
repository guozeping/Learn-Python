# -*- coding:utf-8 -*-
# Created by Guozeping on 2019/10/2
import xlwt

workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('My Sheet')

# 合并单元格
worksheet.write_merge(0, 0, 0, 3, 'First Merge')

font = xlwt.Font()
font.bold = True

style = xlwt.XFStyle()
style.font = font

worksheet.write_merge(1, 2, 0, 3, 'Second Merge', style)

workbook.save('Excel_Workbook_4.xls')