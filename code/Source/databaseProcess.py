# !/usr/bin/env python
# -*- coding: utf-8 -*-
from psycopg2 import connect as psycopg2Connect
from sqlite3 import connect as sqlite3Connect
from datetime import datetime

class databaseOperation():
	def __init__(self, database="menu_debug_data", user="yuanquan", password="yuanquan"):
		self.database = database
		self.user = user
		self.password = password

		self.dataType = """         
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
		self.dataTypeName = ','.join([i.split()[0] for i in self.dataType.split(',') 
										if i.split()!=[] and i.split()[0]!='id'])
		self.sqlite3DbPath = "../sqlite3/database/"
		self.menuMsg = "input"
		self.dbType = "postgre"
		self.dbCon = None

	def databaseOpen(self):
		if self.dbType=="postgre": 
			self.dbCon = psycopg2Connect(database=self.database, user=self.user, password=self.password)
		else : self.dbCon = sqlite3Connect(self.sqlite3DbPath+self.database)
		print("Opened ",self.dbType, self.database, "successfully")

	def databaseClose(self):
		self.dbCon.close()
		if self.dbType=="postgre": 
			print("Closed",self.dbType,"database connect:", self.dbCon.dsn, ",successfully")
		else : 
			print("Closed",self.dbType,"database connect successfully")

	def dbTableInfoInput(self):
		if self.menuMsg=="input": str = input("Please input menu:")
		else: str = "soyMilk"
		if self.menuMsg=="input": str = str+"_"+input("Please materials(g):")+"g"
		else: str = str+'_'+'140'+'g'
		if self.menuMsg=="input": str = str+"_"+input("Please water level(ml):")+"ml"
		else: str = str+'_'+'1400'+'ml'+'_'+datetime.now().strftime('%Y%m%d_%H%M%S')
		return str+'_'+datetime.now().strftime('%Y%m%d_%H%M%S')
	def dbTableCreate(self):
		curConn     = self.dbCon.cursor()    
		tableName   = 'T_'+self.dbTableInfoInput()
		sql         = "CREATE TABLE %s (%s)"%(tableName, self.dataType)+';'
		curConn.execute(sql)
		self.dbCon.commit()
		print('Create table:',tableName,'successfully')
		curConn.close()
		return tableName
	def dbDataWrite(self, curConn, tableName, dat):
		if self.dbType=="postgre": time = 'LOCALTIMESTAMP,'
		else: time = 'CURRENT_TIMESTAMP,'
		sql     = "INSERT INTO %s(%s) values(%s)"%(tableName, self.dataTypeName, time+str(dat)[1:-1]) +';'
		curConn.execute(sql)
		self.dbCon.commit()
	def dbTablesDelete(self, tableNames):
		curConn = self.dbCon.cursor()
		for tableName in tableNames:
			try: 
				curConn.execute("DROP TABLE %s"%(tableName))
				print("Drop table:", tableName, "successfully")
			except:
				print("Drop table:", tableName, "failly")
		self.dbCon.commit()

	def addTableComment(self, tableName):
		comment = input("Pleas input comment for table {}: ".format(str(tableName)))
		commentAdd = self.sqlExe("""SELECT
								description
							FROM
								pg_description
							WHERE 
								pg_description.objoid= (
									SELECT 
										oid 
									FROM 
										pg_class 
									WHERE pg_class.relname='{}')
							""".format(tableName))
		if commentAdd==[]: comment = comment +";"
		else: comment = comment+";"+commentAdd
		print("Comments:", comment)
		self.sqlExe("COMMENT ON TABLE {} IS '{}'".format(tableName, comment))	

	def sqlExe(self, sql):
		curConn   = self.dbCon.cursor()
		curConn.execute(sql)
		try:
			data = curConn.fetchall()
			return data
		except:
			pass
		self.dbCon.commit()