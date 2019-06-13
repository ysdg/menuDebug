# !/usr/bin/env python
# -*- coding: utf-8 -*-
from psycopg2 import connect as psycopg2Connect
from sqlite3 import connect as sqlite3Connect
from datetime import datetime

class databaseOperation():
	""" 
	class for database operation, including:
		open, close based on DB;
		read, write, comment, delete based on tableName.
	 """
	def __init__(self, database="menu_debug_data", user="yuanquan", password="yuanquan"):
		""" 
		database: database name, "menu_debug_data" by default;
		user: database user name, "yuanquan" by default;
		password: database password of user, "yuanquan" by default;
		
		dataType: DB data type init;
		dataTypeName: DB data columens name;
		sqlite3DbPath: the database file relative path if database is sqlite3;
		menuMsg: tablename of DB is input or default;
		dbCon: DB connect.
		 """
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
		""" 
		get connetion of database to self.dbCon, for postgre or sqlite3.
		 """
		if self.dbType=="postgre": 
			self.dbCon = psycopg2Connect(database=self.database, user=self.user, password=self.password)
		else : self.dbCon = sqlite3Connect(self.sqlite3DbPath+self.database)
		print("Opened ",self.dbType, self.database, "successfully")

	def databaseClose(self):
		""" 
		close connetion of database self.dbCon, for postgre of sqlite3.
		 """
		self.dbCon.close()
		if self.dbType=="postgre": 
			print("Closed",self.dbType,"database connect:", self.dbCon.dsn, ",successfully")
		else : 
			print("Closed",self.dbType,"database connect successfully")

	def dbTableInfoInput(self):
		""" 
		input DB table name, for such information:
			menu, materials, waterlevel
		return table name with information and datetime.
		if not input, soymilk, 140g, 1400ml by default.
		 """
		if self.menuMsg=="input":
			tablename = input("Please input menu:")
			tablename = tablename + "_" + input("Please materials(g):") + "g"
			tablename = tablename + "_" + input("Please water level(ml):") + "ml" +'_'
		else:
			tablename = "soyMilk"+'_'+'140'+'g'+'_'+'1400'+'ml'+'_'
		return tablename+datetime.now().strftime('%Y%m%d_%H%M%S')

	def dbTableCreate(self):
		""" 
		create table base on connect of DB;
		return tablename created.
		 """
		curConn     = self.dbCon.cursor()    
		tableName   = 'T_'+self.dbTableInfoInput()
		sql         = "CREATE TABLE %s (%s)"%(tableName, self.dataType)+';'
		curConn.execute(sql)
		self.dbCon.commit()
		print('Create table:',tableName,'successfully')
		curConn.close()
		return tableName

	def dbDataWrite(self, curConn, tableName:str, dat:list):
		""" 
		write dat to DB;
		time format is difference from DB type.
		 """
		if self.dbType=="postgre": time = 'LOCALTIMESTAMP,'
		else: time = 'CURRENT_TIMESTAMP,'
		sql	= "INSERT INTO %s(%s) values(%s)"%(tableName, self.dataTypeName, time+str(dat)[1:-1]) +';'
		curConn.execute(sql)
		self.dbCon.commit()

	def dbTablesDelete(self, tableNames:list):
		""" 
		delete tables based on DB connect.
		 """
		curConn = self.dbCon.cursor()
		for tableName in tableNames:
			try: 
				curConn.execute("DROP TABLE %s"%(tableName))
				print("Drop table:", tableName, "successfully")
			except:
				print("Drop table:", tableName, "failly")
		self.dbCon.commit()

	def addTableComment(self, tableName:str):
		""" 
		add table comment to before.
		 """
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

	def sqlExe(self, sql:str):
		""" 
		execute sql based on DB connect.
		 """
		curConn   = self.dbCon.cursor()
		curConn.execute(sql)
		try:
			data = curConn.fetchall()
		except:
			data = None
		self.dbCon.commit()
		return data
	
	def dbDataRead(self, tableName:str, cols:list):
		""" 
		read data from DB.
		return data list based cols list.
		 """
		data = []
		for col in cols:
			sql = "SELECT {} FROM {}".format(col,tableName)
			data.append(self.sqlExe(sql))
		return data

if __name__ == "__main__":
	dbOperation = databaseOperation()
	dbOperation.databaseOpen()
	sql = """	SELECT 
					tabname
				FROM
					(select relname as tabname,
					cast(obj_description(relfilenode,'pg_class') as varchar) as comment from pg_class c 
					where  relkind = 'r' and relname not like 'pg_%' and relname not like 'sql_%' order by comment) AS C
				WHERE
					comment LIKE '%1#%'
			"""
	print(dbOperation.sqlExe(sql))

	dbOperation.databaseClose()