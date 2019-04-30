# !/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
from filePreDeal import *
from excelWriting import *
from re import split as reSplit

class fileDeal():
	""" 
	deal with file to transfer to excel.
		filename: filename with path, which shoudle be predealed;
		menuNameDict: menu name dictionary, which for writing excel data;
		encoding: UTF-8 by default;
		fopen: cursor of file reading;
	 """
	def __init__(self, filename, menuNameDict={}):
		self.encoding = 'UTF-8'
		self.menuNameDict = menuNameDict
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
			for menuName in list(self.menuNameDict):
				if linedata.find(menuName)!=-1:
					return menuName

			linedata = linedata[linedata.find('{')+1:linedata.find('}')]
			strList = reSplit(",|\(|\)|\|", linedata)
			if '' in strList: strList.remove('')
			return strList
	def fileToExcel(self, excelWb: excelWrite):
		""" 
		transfer file, which out of comment, to excel.
		 """
		for lineData in self.fopen.readlines():
			lineData = ''.join(lineData.split())
			lineDataDealed =  self.dealLineDat(lineData)
			if type(lineDataDealed) is list and lineDataDealed!=[]:
				print(lineDataDealed)
				excelWb.writeRowData(lineDataDealed)
			elif type(lineDataDealed) is str:
				excelWb.createNewSheet(lineDataDealed)
			elif type(lineDataDealed) is int:
				print("something wrong!")
		excelWb.remainTimeProcess()
	def dataTransferReading(self):
		""" 
		read transfer menu name and machine data, which is for writing excel.
		 """
		startReadMenuName = 0
		menuNameDict = {}
		for lineData in self.fopen.readlines():
			lineData = ''.join(lineData.split())
			if lineData.find('machineName')!=-1:
				machineName = lineData[lineData.find("=")+1:]
			if lineData.find('menuNameDict')!=-1:
				startReadMenuName = 1
			if startReadMenuName==1:
				s = (lineData.strip(',')).split(":")
				if len(s) > 1: 
					menuNameDict[s[0]]=s[1]
		return machineName, menuNameDict

def main():
	# os.chdir('.\\'+'src')
	dataTransferFile = fileDeal(filePreDeal(["dataTransfer.txt"])[0])
	machineName, menuNameDict = dataTransferFile.dataTransferReading()

	fileDealing = fileDeal(filePreDeal()[0], menuNameDict)
	excelWritingWb =excelWrite(machineName, menuNameDict)
	fileDealing.fileToExcel(excelWritingWb)
	excelWritingWb.saveExcel()
	fileDealing.fopen.close()
	input("successfully, input any key to end!")
	del dataTransferFile, fileDealing
	os.remove("tmpdataTransfer.txt")
	os.remove("tmpMENU.C")

if __name__ == "__main__":
	main()
