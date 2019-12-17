# -*- coding:utf-8 -*-
# Created by Guozeping on 2019/10/2
import xlwt

workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('My Sheet')

borders = xlwt.Borders()
borders.left = xlwt.Borders.DASHED

borders.right = xlwt.Borders.DASHED
borders.top = xlwt.Borders.DASHED
borders.bottom = xlwt.Borders.DASHED
borders.left_colour= 0x40
borders.right_colour = 0x40
borders.top_colour = 0x40
borders.bottom_colour = 0x40

style = xlwt.XFStyle()
style.borders = borders

worksheet.write(0, 0, 'Cell Contents', style)
workbook.save('Excel_Workbook_5.xls')