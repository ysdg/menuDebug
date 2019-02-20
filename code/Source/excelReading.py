# !/usr/bin/env python
# -*- coding: utf-8 -*-
import xlrd
import os, sys

menuProcessfileName = 'L18-Y920-menuProgramProcess.xlsx'
dataSheetName = u"五谷浆"
os.chdir(sys.path[0])
excelAbsPath = os.path.join(os.path.abspath('..'), 'document', menuProcessfileName)

# read row data from excel by default.
# data from float to secoud: second = float*240*60*60(1 day for 1)
def excelDataRead(count=0, rowOrCol='row'):
    data = xlrd.open_workbook(excelAbsPath)
    table = data.sheet_by_name(dataSheetName)
    if rowOrCol=='col': return table.col_values(count)
    else: return table.row_values(count)

print(excelDataRead(6)[2]*24*60*60)