# -*- coding:utf-8 -*-
# Created by Guozeping on 2019/10/2
import xlwt

workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('My Sheet')

pattern = xlwt.Pattern()
pattern.pattern = xlwt.Pattern.SOLID_PATTERN
pattern.pattern_fore_colour = 5

style = xlwt.XFStyle()
style.pattern = pattern
worksheet.write(0, 0, 'Cell Conters', style)
workbook.save('Excel_Workbook_6.xls')