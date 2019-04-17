# !/usr/bin/env python
# -*- coding: utf-8 -*-
from psycopg2 import connect as psycopg2Connect
from sqlite3 import connect as sqlite3Connect

import numpy as np

# absolute time
from datetime import datetime
time = datetime.now()

# only for sqlite3 database
databasePath= "../sqlite3/database/"
# "default" or "input", default: soyMilk, 140g, 1400ml
menuMsg     = "input"
database    = "menu_debug_data"
user        = "yuanquan"
password    = "yuanquan"
dataType    =   """         
				time        timestamp   NOT NULL,
				header      int         NOT NULL, 
				sysStatus   int         NOT NULL,
				fyValue     int         NOT NULL,
				fyAdStand   int         NOT NULL,
				fyDistance  int         NOT NULL,
				fyFlag      int         NOT NULL,
				curTemp     int         NOT NULL,
				jumpTemp    int         NOT NULL,
				targetTemp  int         NOT NULL,
				motoData    int         NOT NULL,
				heatData    int         NOT NULL,
				motoCur     int         NOT NULL,
				endLine     int         NOT NULL,
				id          SERIAL     PRIMARY KEY
				"""
dataTypeName    = ','.join([i.split()[0] for i in dataType.split(',') 
								if i.split()!=[] and i.split()[0]!='id'])

def databaseOpen(database, user, password, dbType):
	if dbType=="postgre": dbConnect = psycopg2Connect(database=database, user=user, password=password)
	else : dbConnect = sqlite3Connect(databasePath+database)
	print("Opened ",dbType, database, "successfully")
	return dbConnect
def databaseClose(dbConnect, dbType):
	dbConnect.close()
	if dbType=="postgre": print("Closed",dbType,"database connect:", dbConnect.dsn, ",successfully")
	else : print("Closed",dbType,"database connect successfully")
	return 

def dbTableInfoInput(menuMsg="input"):
	if menuMsg=="input": str = input("Please input menu:")
	else: str = "soyMilk"
	if menuMsg=="input": input("Please materials(g):")
		# str = str +'_'+ "Juice"
	else: str = str+'_'+'140'+'g'
	if menuMsg=="input": input("Please water level(ml):")
		#str = str +'_'+"1400"
	else: str = str+'_'+'1400'+'ml'+'_'+datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
	return str+'_'+datetime.now().strftime('%Y_%m_%d_%H_%M_%S')

def dbTableCreate(dbConnect, dataType, dbType='sqlite3'):
	curConn     = dbConnect.cursor()    
	if dbType=="postgre": time = 'LOCALTIMESTAMP,'
	else: time  = 'CURRENT_TIMESTAMP,'
	tableName   = 'T'+dbTableInfoInput(menuMsg)
	sql         = "CREATE TABLE %s (%s)"%(tableName, dataType)+';'
	curConn.execute(sql)
	dbConnect.commit()
	print('Create table:',tableName,'successfully')
	curConn.close()
	return tableName

def dbDataWrite(dbConnect, curConn, tableName, dat, dbType="postgre"):
	if dbType=="postgre": time = 'LOCALTIMESTAMP,'
	else: time = 'CURRENT_TIMESTAMP,'
	sql     = "INSERT INTO %s(%s) values(%s)"%(tableName, dataTypeName, time+str(dat)[1:-1]) +';'
	curConn.execute(sql)
	dbConnect.commit()
	return 

def dbTableDelete(tableToDelete, database=database, dbType='sqlite3'):
	dbConnect   = databaseOpen(database, user, password, dbType)
	curConn     = dbConnect.cursor()
	for tableName in tableToDelete:
		try: 
			curConn.execute("DROP TABLE %s"%(tableName))
			print("Drop table:", tableName, "successfully")
		except:
			print("Drop table:", tableName, "failly")
	dbConnect.commit()
	curConn.close()
	databaseClose(dbConnect, dbType)

# read data from database
# clomune = [] means return all and clomune must be a list
def dbDataRead(tableName, clomune=[], dbType='sqlite3'):
	dbConnect   = databaseOpen(database, user, password, dbType)
	curConn     = dbConnect.cursor()
	data        = []
	for cloName in clomune:
		sql = "SELECT %s FROM %s"%(cloName, tableName)
		curConn.execute(sql)
		data.append([a[0] for a in curConn.fetchall()])
	if clomune==[]: 
		sql = "SELECT * FROM %s"%tableName
		curConn.execute(sql)
		data.append([a for a in curConn.fetchall()])
	dbConnect.commit()
	curConn.close()
	databaseClose(dbConnect, dbType)
	return data

def sqlExe(sql, dbCon, dbType='sqlite3'):
	curConn   = dbCon.cursor()
	curConn.execute(sql)
	data      = curConn.fetchall()
	dbCon.commit()
	return data

def dataTableProcess(tableNames):
	tableNameReturn = []
	for tableName in tableNames:
		tableNameSeq = tableName.split('_')
		if  len(tableNameSeq)>5     and \
			tableNameSeq[3]=='2019' and \
			tableNameSeq[4]=='02'   and \
			tableNameSeq[5]=='25':
			if  (tableNameSeq[0]=='TmotoL10' and tableNameSeq[1]=='soyMilk'):
				# (tableNameSeq[0]=='TmotoL11' and tableNameSeq[1]=='soyMilk'  and tableNameSeq[2]=='700') or \
				# (tableNameSeq[0]=='TmotoL11' and tableNameSeq[1]=='Juice'    and tableNameSeq[2]=='1400') :
				tableNameReturn.append(tableName)
	for i in range(len(tableNameReturn)-2):
		if len(tableNameReturn)<3 or i>=len(tableNameReturn): break
		before = tableNameReturn[i].split('_')
		after = tableNameReturn[i+1].split('_')
		if before[0]==after[0] and before[1]==after[1] and before[2]==after[2]:
			del tableNameReturn[i]
	# del tableNameReturn[1:4]
	return tableNameReturn
		

def sqlDebug(dbType):
	dbConnect   = databaseOpen(database, user, password, dbType)
	curConn     = dbConnect.cursor()
	# tableName   = dbTableCreate(dbConnect, dataType)
	# data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
	# dbDataWrite(dbConnect, curConn, tableName, data, dbType)
	# sql = "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;"
	# curConn.execute(sql)
	# tableNames = [a[0] for a in curConn.fetchall()]
	# print(tableNames)
	sql = "SELECT name FROM sqlite_master"
	curConn.execute(sql)
	# print(curConn.fetchall())
	print([i[1] for i in curConn.fetchall()])
	# dbConnect.commit()
	# tableSetNames = [a[0] for a in curConn.fetchall()]
	# print(tableSetNames)
	# for table in tableSetNames:
	#     sql = "SELECT id FROM %s"%table
	#     curConn.execute(sql)
	#     print(max([a[0] for a in curConn.fetchall()]))
	# sql = "DROP TABLE TsoyMilk_140g_1400ml_2018_12_29_11_43_17"
	
	# print(tableSetNames)
	# print([a[1] for a in curConn.fetchall()])

	dbConnect.commit()
	curConn.close()
	databaseClose(dbConnect, dbType)

# sqlDebug("sqlite3")
# dataTableNames = [i[0] for i in sqlExe("SELECT name FROM sqlite_master") if i[0]!='sqlite_sequence']
# for i in dataTableProcess(dataTableNames):
#     data = dbDataRead(i, ['motoCur'])
#     print(i,'--',np.mean(data))
# print(dataTableNames)
# print(sqlExe("SELECT name FROM sqlite_master      \
#                 WHERE type='table' and rowid=(SELECT MAX(rowid) FROM sqlite_master)"))