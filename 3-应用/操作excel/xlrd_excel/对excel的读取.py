# -*- coding:utf-8 -*-
# Created by Guozeping on 2019/10/2
import xlrd

# 打开excel文件读取数据
data = xlrd.open_workbook('Excel_Workbook_5.xls')
# 获取一个工作表
table = data.sheets()  # 通过索引顺序获取
# table = data.sheet_by_index(0)  # 通过索引顺序获取
# table = data.sheet_by_name(u'Sheet1')  # 通过名称获取

# 获取整行和整列的值（返回数组）
table.row_values()
table.col_values()

# # 获取行数和列数
# table.nrows
# table.ncols
#
# # 获取单元格
# table.cell(0,0).value
# table.cell(2,3).value
