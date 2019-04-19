# !/usr/bin/env python
# -*- coding: utf-8 -*-
from serial import Serial as serialSerial
from databaseProcess import *
from matPlotFromDb import *

# must be "postgre" or "sqlite3"
dbType          = "postgre"

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
		self.UartRxLineHead = 250
		self.UartRxLineEnd = 10
		self.serSize = len(dataTypeName.split(','))
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

	def uartDbWrite(self, dbConnect, dbType):
		""" 
		keep reading uart data, create table and write to db
		dbConnect: database connect;
		dbType: database type;
		 """
		curConn = dbConnect.cursor()
		data    = self.uartDataProcess()
		writeCnt= 0
		while(data != []):
			if data[0]==self.UartRxLineHead and data[-1]==self.UartRxLineEnd and len(data)==len(dataTypeName.split(','))-1: 
				if writeCnt==0:
					self.tablename = dbTableCreate(dbConnect, dataType, dbType)
				dbDataWrite(dbConnect, curConn, self.tablename, data, dbType)
				writeCnt = writeCnt + 1
				print("Write", dbType, "successfully:", data)
			data = self.uartDataProcess()

def main():
	ser         = serialProcess()
	dbConnect   = databaseOpen(database, user, password, dbType)
	try: 
		while 1: 
			ser.uartDbWrite(dbConnect, dbType)
	except  KeyboardInterrupt:
		if ser.tablename!=None:
			if len(sqlExe("SELECT id FROM %s"%(ser.tablename), dbCon=dbConnect,dbType=dbType))<30: 
				dbTableDelete([ser.tablename])
			else: 
				addTableComment(ser.tablename, dbConnect, dbType)

	dbConnect.commit()
	databaseClose(dbConnect, dbType)
	ser.close()

if __name__=='__main__':
	main()