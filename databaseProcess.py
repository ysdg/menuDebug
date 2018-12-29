import psycopg2
import sqlite3

# absolute time
from datetime import datetime
time = datetime.now()

# only for sqlite3 database
databasePath= "./sqlite3/database/"
# "default" or "input", default: soyMilk, 140g, 1400ml
menuMsg     = "default"
database    = "menuDebugData"
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
                remainTime  int         NOT NULL,
                workedTime  int         NOT NULL,
                endLine     int         NOT NULL,
                id          integer     PRIMARY KEY AUTOINCREMENT
                """
dataTypeName    = ','.join([i.split()[0] for i in dataType.split(',') if i.split()!=[] and i.split()[0]!='id'])

def databaseOpen(database, user, password, dbType):
    if dbType=="postgre": dbConnect = psycopg2.connect(database=database, user=user, password=password)
    else : dbConnect = sqlite3.connect(databasePath+database)
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
    if menuMsg=="input": str = input("Please materials(g):")
    else: str = str+'_'+'140'+'g'
    if menuMsg=="input": str = input("Please water level(ml):")
    else: str = str+'_'+'1400'+'ml'+'_'+datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    return str

def dbTableCreate(dbConnect, dataType, dbType='sqlite3'):
    curConn     = dbConnect.cursor()    
    if dbType=="postgre": time = 'LOCALTIMESTAMP,'
    else: time  = 'CURRENT_TIMESTAMP,'
    tableName   = 'T'+dbTableInfoInput(menuMsg)
    sql         = "CREATE TABLE %s (%s)"%(tableName, dataType)+';'
    curConn.execute(sql)
    sql = "INSERT INTO tableSet(time,tableName) values(%s)"%(time+"'"+tableName+"'")
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

def dbTableDelete(database, tableToDelete, dbType='sqlite3'):
    dbConnect   = sqlite3.connect(databasePath+database)
    curConn     = dbConnect.cursor()
    for tableName in tableToDelete:
        curConn.execute("DROP TABLE %s"%(tableName))
        curConn.execute("DELETE * FROM tableSet WHERE tableName=%s"%("'"+tableName+"'"))
        print("Drop table:", tableName, "successfully")
    dbConnect.commit()
    curConn.close()
    databaseClose(dbConnect, dbType)

def sqlDebug(dbType):
    dbConnect   = databaseOpen(database, user, password, dbType)
    curConn     = dbConnect.cursor()
    # tableName   = dbTableCreate(dbConnect, dataType)
    # data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    # dbDataWrite(dbConnect, curConn, tableName, data, dbType)
    # sql         = """CREATE TABLE tableSet( id          integer     PRIMARY KEY AUTOINCREMENT,
    #                                         tableName   text NOT NULL, 
    #                                         time        timestamp   NOT NULL)"""
    # sql = "INSERT INTO tableSet(time,tableName) values(%s)"%("CURRENT_TIMESTAMP, 't12_23dad_'")
    # sql = "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;"
    # curConn.execute(sql)
    # tableNames = [a[0] for a in curConn.fetchall()]
    # print(tableNames)
    sql = "SELECT tableName FROM tableSet"
    curConn.execute(sql)
    tableSetNames = [a[0] for a in curConn.fetchall()]
    print(tableSetNames)
    for table in tableSetNames:
        sql = "SELECT id FROM %s"%table
        curConn.execute(sql)
        print(max([a[0] for a in curConn.fetchall()]))
    # sql = "DELETE FROM tableSet WHERE tableName='TsoyMilk_140g_1400ml_2018_12_29_11_43_17'"
    # sql = "DROP TABLE TsoyMilk_140g_1400ml_2018_12_29_11_43_17"
    # curConn.execute(sql)
    # curConn.execute("DROP TABLE tableSet")
    # print(tableSetNames)
    # print([a[1] for a in curConn.fetchall()])

    dbConnect.commit()
    curConn.close()
    databaseClose(dbConnect, dbType)

# sqlDebug("sqlite3")