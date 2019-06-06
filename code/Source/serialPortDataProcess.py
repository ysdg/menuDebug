# !/usr/bin/env python
# -*- coding: utf-8 -*-
from serial import Serial as serialSerial
from databaseProcess import *
from matPlotFromDb import *

class serialProcess(serialSerial):
	""" 
	based on serialSerial;
	the class is for serial data process.
	 """
	def __init__(self, serPort="COM5", serPortBold=9600):
		""" 
		serPort, serPortBold: for serialSerial
		others: my own definetion
		"""
		super(serialProcess, self).__init__(serPort, serPortBold)

		self.DB = databaseOperation()
		self.UartRxLineHead = 250
		self.UartRxLineEnd = 10
		self.serSize = len(self.DB.dataTypeName.split(','))
		self.tablename = None
	
	def uartDataProcess(self):
		""" 
		deal with oneline serial reading data;
		data[-3] is high Byte of moto current data;
		data[-2] is lower Byte of moto current .
		 """
		data = [i for i in self.readline(self.serSize)]
		if(data == []): return []
		while len(data)<self.serSize: data = data + [i for i in self.readline(self.serSize)]
		data =  data[:-3] +  [data[-3]*256+data[-2], data[-1]]
		return data

	def uartDbWrite(self):
		""" 
		keep reading uart data, create table and write to db
		dbConnect: database connect;
		dbType: database type;
		 """
		curConn = self.DB.dbCon.cursor()
		data    = self.uartDataProcess()
		writeCnt= 0
		while(data != []):
			if 	data[0]==self.UartRxLineHead and \
				data[-1]==self.UartRxLineEnd and \
				len(data)==len(self.DB.dataTypeName.split(','))-1: 
				if writeCnt==0:
					self.tablename = self.DB.dbTableCreate()
				self.DB.dbDataWrite(curConn, self.tablename, data)
				writeCnt = writeCnt + 1
				print("Write", self.DB.dbType, "successfully:", data)
			data = self.uartDataProcess()

def main():
	ser = serialProcess()
	ser.DB.databaseOpen()
	try: 
		while 1: 
			ser.uartDbWrite()
	except  KeyboardInterrupt:
		if ser.tablename!=None:
			if len(ser.DB.sqlExe("SELECT id FROM %s"%(ser.tablename)))<30: 
				ser.DB.dbTablesDelete([ser.tablename])
			else: 
				ser.DB.addTableComment(ser.tablename)
	ser.DB.databaseClose()
	ser.close()

if __name__=='__main__':
	main()
	# print(help(serialProcess))