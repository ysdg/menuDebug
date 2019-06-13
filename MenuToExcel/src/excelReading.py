# !/usr/bin/env python
# -*- coding: utf-8 -*-
""" excel reading class based on openpyxl """
import openpyxl
import os, sys

class excelRead():
	""" class deal with excel reading based on openpyxl """
	def __init__(self, fileName=None):
		self.fileName = fileName
		self.readOnly = True
		self.curSheet = None

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

# read row data from excel by default.
# data from float to secoud: second = float*240*60*60(1 day for 1)
if __name__ == "__main__":
	excelReading = excelRead()
	excelReading.fileGetAndLoad()
	excelReading.curSheet = excelReading.wb[excelReading.wb.sheetnames[0]]
	excelReading.sheetDatRead()
	print(excelReading.curSheetDat)