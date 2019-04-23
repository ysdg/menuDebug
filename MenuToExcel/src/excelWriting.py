# !/usr/bin/env python
# -*- coding: utf-8 -*-
import openpyxl
from dataTransfer import *
from datetime import datetime

class excelWrite(openpyxl.Workbook):
	def __init__(self):
		super(excelWrite, self).__init__()
		print("open excel work book successfully.")
		self.excelColName = ['步骤', '功能', '步骤时间', '倒计时', '备注']
		self.excelName = machineName+"菜单流程"+datetime.now().strftime('%Y%m%d_%H%M%S')+".xlsx"
		self.align = openpyxl.styles.Alignment(horizontal='right',vertical='center',wrap_text=True)
		self.sheetIndex = 0
		self.excelRelativePath = "../"
	def saveExcel(self):
		self.save(self.excelName)
		print("save excel: "+self.excelName+", successfully.")
	def rowData(self, step, ctrlMess, stepTime, remainTime, endCondition):
		dat = [step, ctrlMess, stepTime, remainTime, endCondition]
	def createNewSheet(self, nameKey):
		self.curSheet = self.create_sheet(menuNameDict[nameKey])
		self.curSheetRow = 1
		print("Create sheet: "+menuNameDict[nameKey]+", successfully.")
		if self.sheetnames[0]=="Sheet": self.remove(self["Sheet"])
	def rowAlignSet(self):
		self.curSheet['A'+str(self.curSheetRow)].alignment = self.align
		self.curSheet['B'+str(self.curSheetRow)].alignment = self.align
		self.curSheet['C'+str(self.curSheetRow)].alignment = self.align
		self.curSheet['D'+str(self.curSheetRow)].alignment = self.align
		self.curSheet['E'+str(self.curSheetRow)].alignment = self.align
		self.curSheet.column_dimensions['A'].width = 10
		self.curSheet.column_dimensions['B'].width = 30
		self.curSheet.column_dimensions['C'].width = 15
		self.curSheet.column_dimensions['D'].width = 15
		self.curSheet.column_dimensions['E'].width = 30
	def writeRowData(self, dat):
		step = self.curSheetRow-1
		if  dat == ['0', '0', '0', '0', '0'] or dat==[]: 
			self.curSheetRow = self.curSheetRow+1
			return 
		if self.curSheetRow==1:
			self.curSheet.append(self.excelColName)
			self.rowAlignSet()
			self.curSheetRow = self.curSheetRow+1
			return

		if  dat[1].find("Temp")!=-1 and \
			dat[1].find("TEMP")!=-1 and \
			dat[1].find("temp")!=-1:
			if dat[0] in list(workHeadDictH)[5:10]:
				if dat[-2] in list(heatRankDict):
					ctrlMess = heatRankDict[dat[-2]]+'档加热至'+dat[-1]+'度'+'\n'+'('+workHeadDictH[dat[0]]+')'
			elif dat[0]==list(workHeadDictH)[2]:
				ctrlMess = heatRankDict[dat[-2]]+'档'+workHeadDictH[dat[0]]+'至'+dat[-1]+'度'
			elif dat[0]==list(workHeadDictH)[1]:
				ctrlMess = heatRankDict[dat[-1]]+'档'+workHeadDictH[dat[0]]
			elif dat[0]==list(workHeadDictH)[0]:
				ctrlMess = workHeadDictH[dat[0]]
			elif dat[0]==list(workHeadDictH)[4]:
				ctrlMess = workHeadDictH[dat[0]]+'上'+dat[-2]+'到'+dat[-1]+'步'
			else: ctrlMess = dat[0]
		else:
			if dat[0] in list(workHeadDictH)[5:10]:
				if dat[-2] in list(heatRankDict):
					ctrlMess = heatRankDict[dat[-2]]+'档加热'+'\n'+'('+workHeadDictH[dat[0]]+')'
			elif dat[0]==list(workHeadDictH)[2]:
				ctrlMess = heatRankDict[dat[-2]]+'档'+workHeadDictH[dat[0]]
			elif dat[0]==list(workHeadDictH)[1]:
				ctrlMess = heatRankDict[dat[-1]]+'档'+workHeadDictH[dat[0]]
			elif dat[0]==list(workHeadDictH)[0]:
				ctrlMess = workHeadDictH[dat[0]]
			elif dat[0]==list(workHeadDictH)[4]:
				ctrlMess = workHeadDictH[dat[0]]+'上'+dat[-2]+'到'+dat[-1]+'步'
			else: ctrlMess = workHeadDictH[dat[0]]

		if int(dat[3]) > 60: stepTime = '01:'+str(int(dat[3])-60).zfill(2)+':'+str(int(dat[4])).zfill(2)
		else: stepTime = '00:'+str(int(dat[3])).zfill(2)+':'+str(int(dat[4])).zfill(2)
		remainTime = "00:00:00"
		endCondition = workHeadDictL[dat[1]]
		self.curSheet.append([step, ctrlMess, stepTime, remainTime, '以'+endCondition])
		self.curSheet.cell(self.curSheetRow, column=3).number_format = openpyxl.styles.numbers.FORMAT_DATE_TIME6
		self.rowAlignSet()
		self.curSheetRow = self.curSheetRow+1


if __name__=="__main__":
	pass

