# !/usr/bin/env python
# -*- coding: utf-8 -*-
import openpyxl
from dataTransfer import *
from datetime import datetime

excelRelativePath = "../"
sheetIndex = 0
excelName = machineName+"菜单流程"+datetime.now().strftime('%Y%m%d_%H%M%S')+".xlsx"
excelColName = ['步骤', '功能', '步骤时间', '倒计时', '备注']
align = openpyxl.styles.Alignment(horizontal='right',vertical='center',wrap_text=True)

class RowData():
	def __init__(self, step, ctrlMess, stepTime, remainTime, endCondition):
		self.step = step
		self.ctrlMess = ctrlMess
		self.stepTime = stepTime
		self.remainTime = remainTime
		self.endCondition = endCondition
	def toList(self):
		return [self.step, self.ctrlMess, self.stepTime, self.remainTime, self.endCondition]

def openExcelWorkBook(writeOnly=False):
	wb = openpyxl.Workbook(write_only=writeOnly)
	print("open excel work book successfully.")
	return wb
def saveExcelWorkBook(workBook, Name = excelName):
	workBook.save(Name)
	print("save excel: "+Name+", successfully.")
def createNewSheet(workBook, nameKey='MENU1'):
	workBook.create_sheet(menuNameDict[nameKey])
	print("Create sheet: "+menuNameDict[nameKey]+", successfully.")
	if workBook.sheetnames[0]=="Sheet": workBook.remove(workBook["Sheet"])
	return workBook[menuNameDict[nameKey]]
def writeRowData(sheet, row, values):
	step = row
	if values == ['0', '0', '0', '0', '0'] or values==[]: return 0
	if row==1:
		sheet.append(excelColName)
		sheet['A'+str(row)].alignment = align
		sheet['B'+str(row)].alignment = align
		sheet['C'+str(row)].alignment = align
		sheet['D'+str(row)].alignment = align
		sheet['E'+str(row)].alignment = align
	if values[0] in list(workHeadDictH)[5:10]:
		if values[-2] in list(heatRankDict):
			ctrlMess = heatRankDict[values[-2]]+'档加热'+'\n'+'('+workHeadDictH[values[0]]+')'
	elif values[0]==list(workHeadDictH)[2]:
		ctrlMess = heatRankDict[values[-2]]+'档'+workHeadDictH[values[0]]
	elif values[0]==list(workHeadDictH)[1]:
		ctrlMess = heatRankDict[values[-1]]+'档'+workHeadDictH[values[0]]
	elif values[0]==list(workHeadDictH)[0]:
		ctrlMess = workHeadDictH[values[0]]
	elif values[0]==list(workHeadDictH)[4]:
		ctrlMess = workHeadDictH[values[0]]+'上'+values[-2]+'到'+values[-1]+'步'
	else: ctrlMess = values[0]
	if int(values[3]) > 60: stepTime = '01:'+str(int(values[3])-60).zfill(2)+':'+str(int(values[4])).zfill(2)
	else: stepTime = '00:'+str(int(values[3])).zfill(2)+':'+str(int(values[4])).zfill(2)
	remainTime = 0
	endCondition = workHeadDictL[values[1]]
	sheet.append(RowData(step, ctrlMess, stepTime, remainTime, '以'+endCondition).toList())
	sheet.cell(row, column=3).number_format = openpyxl.styles.numbers.FORMAT_DATE_TIME6

	sheet['A'+str(row+1)].alignment = align
	sheet['B'+str(row+1)].alignment = align
	sheet['C'+str(row+1)].alignment = align
	sheet['D'+str(row+1)].alignment = align
	sheet['E'+str(row+1)].alignment = align


if __name__=="__main__":
	wb = openExcelWorkBook()
	curSheet = createNewSheet(wb, "MENU1")
	# curSheet.alignments = openpyxl.styles.Alignment(horizontal="center", vertical="center", wrap_text=True)
	writeRowData(curSheet, 1, ['OB_H_60S_M_5S', 'Time_OR_Temp', 'TIME_x_M_y_S', '20', '00', 'HEAT_L1_0_0', 'Temp80'])
	
	curSheet.column_dimensions['A'].width = 10
	curSheet.column_dimensions['B'].width = 30
	curSheet.column_dimensions['C'].width = 15
	curSheet.column_dimensions['D'].width = 15
	curSheet.column_dimensions['E'].width = 30

	# curSheet.alignment = align
	saveExcelWorkBook(wb)

