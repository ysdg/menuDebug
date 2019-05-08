# !/usr/bin/env python
# -*- coding: utf-8 -*-
""" excel reading class based on openpyxl """
import openpyxl
import os, sys
from datetime import datetime
from re import findall as reFindall
try: from dataTransfer import *
except: from .dataTransfer import *

class excelRead():
	""" class deal with excel reading based on openpyxl """
	def __init__(self, fileName=None):
		self.fileName = fileName
		self.readOnly = True
		self.curSheet = None
		self.fopen = None

	def fileGetAndLoad(self):
		""" get and load the last excel in relative path. """
		relativePath = "/./"
		dirLists = os.listdir(os.getcwd()+relativePath)
		for dirList in dirLists:
			if dirList.split('.')[-1] == 'xlsx': self.fileName = dirList
		if self.fileName == None:  exit("There is no excel file, please check your path!")
		self.wb = openpyxl.load_workbook(self.fileName, self.readOnly)
		print("open excel {} successfully.".format(self.fileName))
		del dirLists

	def sheetDatRead(self):
		""" read all data from current sheet. """
		self.curSheetDat = []
		self.curRowDat = []
		for row in self.curSheet.rows:
			for cell in row:
				self.curRowDat.append(cell.value)
			self.curSheetDat.append(self.curRowDat)
			self.curRowDat = []

	def get_key(self, dictSearch:dict, value):
		""" get the key list according to value. """
		return [k for k, v in dictSearch.items() if v==value]

	def rowdatRecode(self, rowDat:list):
		""" recode the row dat to c51 code. """
		self.recodeRowDat = []
		headH, headL, stepTime, ctrlMode, ctrlTarget = 1, 4, 2, 1, 1

		valueTmpHeadH = None
		for value in workHeadDictH.values():
			if value!=workHeadDictH[list(workHeadDictH)[1]] and value!=workHeadDictH[list(workHeadDictH)[2]]:
				if rowDat[headH].find(value)!=-1:
					valueTmpHeadH = value
					break
			else:
				if rowDat[headH].find(value)!=-1: 
					valueTmpHeadH = value
		if valueTmpHeadH != None: self.recodeRowDat.append(self.get_key(workHeadDictH, valueTmpHeadH)[0])
		else: return

		for value in workHeadDictL.values():
			if rowDat[headL].find('(')==-1: 
				if rowDat[headL] == "以{}".format(value):
					self.recodeRowDat.append(self.get_key(workHeadDictL, value)[0])
					break
			else:
				if rowDat[headL][:rowDat[headL].find('(')] == "以{}".format(value):
					self.recodeRowDat.append(self.get_key(workHeadDictL, value)[0])
					break
		
		timeFormat = "%H:%M:%S"
		stepDatetime = datetime.strptime(rowDat[stepTime], timeFormat)
		self.recodeRowDat.append("TIME_x_M_y_S({}, {})".format(stepDatetime.hour*60+stepDatetime.minute, stepDatetime.second))

		if self.recodeRowDat[0]==list(workHeadDictH)[2] or \
			self.recodeRowDat[0] in list(workHeadDictH)[5:10]:#heater
			rank = float(reFindall(r"\d+\.?\d*", rowDat[headH])[0])
			self.recodeRowDat.append("HEAT_L{}_{}_{}".format(int(rank/10), int(rank%10), int(rank*10%10)))
		elif self.recodeRowDat[0]==list(workHeadDictH)[1] or \
			self.recodeRowDat[0]==list(workHeadDictH)[-2]:#motor
			self.recodeRowDat.append("MOTOR_MODE")
		elif self.recodeRowDat[0]==list(workHeadDictH)[4]:#repeat
			rank = int(reFindall(r"\d+\.?\d*", rowDat[headH])[0])
			self.recodeRowDat.append(str(rank))
		else: self.recodeRowDat.append("0")
		
		if rowDat[headL].find("更新时间")!=-1:
			self.recodeRowDat.append('DISP_UPDATE')
		else:
			if self.recodeRowDat[0]==list(workHeadDictH)[1] or \
				self.recodeRowDat[0]==list(workHeadDictH)[-2]: #motor
				rank = int(reFindall(r"\d+\.?\d*", rowDat[headH])[0])
				self.recodeRowDat.append("L{}".format(str(rank).replace('.', '_')))
			elif self.recodeRowDat[0] in list(workHeadDictH)[5:-1] or \
				self.recodeRowDat[0]==list(workHeadDictH)[2]: #heater
				try: rank = int(reFindall(r"\d+\.?\d*", rowDat[headH])[1])
				except: rank = 0
				self.recodeRowDat.append(str(rank))
			elif self.recodeRowDat[0]==list(workHeadDictH)[4]:
				rank = int(reFindall(r"\d+\.?\d*", rowDat[headH])[1])
				self.recodeRowDat.append(str(rank))
			else:self.recodeRowDat.append('0')

	def fileCreate(self):
		self.codeFileName = 'MENU.C'
		self.codeFileEncoding = 'UTF-8'
		self.fopen = open(self.codeFileName, 'w', encoding=self.codeFileEncoding)
		for rowdat in self.curSheetDat:
			self.rowdatRecode(rowdat)
			if len(self.recodeRowDat)==5:
				workHead = "{}|{},".format(self.recodeRowDat[0], self.recodeRowDat[1])
				stepTime = "{},".format(self.recodeRowDat[2])
				ctrlMode = self.recodeRowDat[3]
				ctrlTarget = self.recodeRowDat[4]
				self.fopen.write("\t{{{:<35s}{:<25s}{:<15s},{:<15s}}},".format(workHead, stepTime, ctrlMode, ctrlTarget))
			# for dat in self.recodeRowDat:
			# 	if dat!=None: self.fopen.write("{:<10s} ".format(str(dat).replace('\n', '_')))
			self.fopen.write('\n')
		self.fopen.close()

def main():
	excelReading = excelRead()
	excelReading.fileGetAndLoad()
	excelReading.curSheet = excelReading.wb[excelReading.wb.sheetnames[0]]
	excelReading.sheetDatRead()
	print(excelReading.curSheetDat)	
	excelReading.fileCreate()

# read row data from excel by default.
# data from float to secoud: second = float*240*60*60(1 day for 1)
if __name__ == "__main__":
	main()