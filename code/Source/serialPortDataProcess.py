# !/usr/bin/env python
# -*- coding: utf-8 -*-
from serial import Serial as serialSerial
from databaseProcess import *
from matPlotFromDb import *

# must be "postgre" or "sqlite3"
dbType          = "postgre"
serPort         = "COM5"
serPortBold     = 9600
serSize         = len(dataTypeName.split(','))
timeOut         = 1.5
UartRxLineHead  = 250
UartRxLineEnd   = 10

def uartDataProcess(ser):
	data = [i for i in ser.readline(serSize)]
	if(data == []): return []
	while len(data)<serSize: data = data + [i for i in ser.readline(serSize)]
	data =  data[:-3] +  \
			[   data[-3]*256+data[-2],
				data[-1]  ]
	return data

def uartDbWrite(ser, dbConnect, dbType):
	curConn = dbConnect.cursor()
	data    = uartDataProcess(ser)
	writeCnt= 0
	while(data != []):
		if data[0]==UartRxLineHead and data[-1]==UartRxLineEnd and len(data)==len(dataTypeName.split(','))-1: 
			if writeCnt==0:
				tableName = dbTableCreate(dbConnect, dataType, dbType)
			dbDataWrite(dbConnect, curConn, tableName, data, dbType)
			writeCnt = writeCnt + 1
			print("Write", dbType, "successfully:", data)
		data = uartDataProcess(ser)
	if writeCnt > 0:
		if writeCnt < 30:
			curConn.execute("DROP TABLE %s"%tableName)
			print("Drop table:", tableName, "successfully")
		# else: tableDatPlot(tableName)
	dbConnect.commit()
	curConn.close()
	if writeCnt > 0: return tableName
	else: return 

def main():
	ser         = serialSerial(serPort, serPortBold, timeout=timeOut)
	dbConnect   = databaseOpen(database, user, password, dbType)
	
	# for tableName in tableNames: 
	# 	if sqlExe("SELECT id FROM %s"%(tableName))==[]: dbTableDelete([tableName])
	try: 
		while 1: 
			tableName = uartDbWrite(ser, dbConnect, dbType)
	except  KeyboardInterrupt:
		if tableName!=None:
			if sqlExe("SELECT id FROM %s"%(tableName), dbCon=dbConnect,dbType=dbType)==[]: 
				dbTableDelete([tableName])
	databaseClose(dbConnect, dbType)
	ser.close()

if __name__=='__main__':
	main()