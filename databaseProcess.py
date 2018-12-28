import psycopg2
import sqlite3

# absolute time
from datetime import datetime
time = datetime.now()

# only for sqlite3 database
databasePath= "E:\\工艺调试\\sqlite3\\database\\"
database    = "test"
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

def dbTableInfoInput():
    print("Please input menu:")
    str = input()
    print("Please materials(g):")
    str = str+'_'+input()+'g'
    print("Please water level(ml):")
    str = str+'_'+input()+'ml'+'_'+datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    return str

def dbTableCreate(dbConnect, dataType):
    curConn     = dbConnect.cursor()    
    tableName   = 'T'+dbTableInfoInput()
    sql         = "CREATE TABLE %s (%s)"%(tableName, dataType)+';'
    curConn.execute(sql)
    dbConnect.commit()
    curConn.close()
    return tableName

def dbDataWrite(dbConnect, curConn, tableName, dat, dbType="postgre"):
    if dbType=="postgre": time = 'LOCALTIMESTAMP,'
    else: time = 'CURRENT_TIMESTAMP,'
    sql     = "INSERT INTO %s(%s) values(%s)"%(tableName, dataTypeName, time+str(dat)[1:-1]) +';'
    curConn.execute(sql)
    dbConnect.commit()
    return 

def sqlDebug(dbType):
    dbConnect   = databaseOpen(database, user, password, dbType)
    curConn     = dbConnect.cursor()
    # tableName   = dbTableCreate(dbConnect, dataType)
    # data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    # dbDataWrite(dbConnect, curConn, tableName, data, dbType)
    sql         = "SELECT * FROM sqlite_master WHERE type='table' ORDER BY name"
    curConn.execute(sql)
    print([a[1] for a in curConn.fetchall()])
    # print([a[1] for a in curConn.fetchall()])

    dbConnect.commit()
    curConn.close()
    databaseClose(dbConnect, dbType)

# sqlDebug("sqlite3")