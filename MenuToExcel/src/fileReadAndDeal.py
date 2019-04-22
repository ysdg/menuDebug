# !/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
from filePreDeal import *
from dataTransfer import *
from excelWriting import *
from re import split as reSplit

class fileDeal():
	def __init__(self, filename):
		self.encoding = 'UTF-8'
		self.fopen = open(filename, 'r', encoding=self.encoding)
	
	def dealLineDat(self, linedata:str):
		"""
		deal with one line data from file data after pretreament;
		return :
			int -1 for wrong data;
			str for MENU name;
			list for menu useful data.
		"""
		if linedata.isspace(): return -1
		else:
			for menuName in list(menuNameDict):
				if linedata.find(menuName)!=-1:
					return menuName

			linedata = linedata[linedata.find('{')+1:linedata.find('}')]
			strList = reSplit(",|\(|\)|\|", linedata)
			if '' in strList: strList.remove('')
			return strList		

def main():
	# os.chdir('.\\'+'src')
	fileDealing = fileDeal(filePreDeal()[0])
	wb = openExcelWorkBook()
	sheetRowIndex = 1
	# for i in range(len(menuNameDict)):
		# menuName = list(menuNameDict)[i]
		# lineData = f.readline()
	for lineData in fileDealing.fopen.readlines():
		lineData = ''.join(lineData.split())
		lineDataDealed =  fileDealing.dealLineDat(lineData)
		if type(lineDataDealed) is list and lineDataDealed!=[]:
			print(lineDataDealed)
			writeRowData(curSheet, sheetRowIndex, lineDataDealed)
			sheetRowIndex = sheetRowIndex+1
		elif type(lineDataDealed) is str:
			try: 
				curSheet.column_dimensions['A'].width = 10
				curSheet.column_dimensions['B'].width = 30
				curSheet.column_dimensions['C'].width = 15
				curSheet.column_dimensions['D'].width = 15
				curSheet.column_dimensions['E'].width = 30
			except: pass
			curSheet = createNewSheet(wb, lineDataDealed)
			sheetRowIndex = 1
		elif type(lineDataDealed) is int:
			print("something wrong!")
	curSheet.column_dimensions['A'].width = 10
	curSheet.column_dimensions['B'].width = 30
	curSheet.column_dimensions['C'].width = 15
	curSheet.column_dimensions['D'].width = 15
	curSheet.column_dimensions['E'].width = 30
	saveExcelWorkBook(wb)

		
	# lineData = "{OB_Motor|End_Time,TIME_x_M_y_S(0,10),MOTOR_MODE,L1},"
	
	fileDealing.fopen.close()
	input("successfully, input any key to end!")

if __name__ == "__main__":
	main()
