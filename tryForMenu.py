import sqlite3

# absolute time
from datetime import datetime
time = datetime.now()

databasePath= "E:\\工艺调试\\sqlite3\\database\\"
database    = "test"
dataType    =   """
                time        timestamp   PRIMARY KEY,
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
                endLine     int         NOT NULL
                """
dataTypeName    = ','.join([i.split()[0] for i in dataType.split(',') if i.split()!=[]])

def databaseOpen(database):
    dbConnect   = sqlite3.connect(databasePath+database)
    print("Opened database", database, "successfully")
    return dbConnect
def databaseClose(dbConnect):
    dbConnect.close()
    print("Closed database connect successfully")
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

def dbDataWrite(dbConnect, curConn, tableName, dat): 
    sql     = "INSERT INTO %s(%s) values(%s)"%(tableName, dataTypeName, 'LOCALTIMESTAMP,'+str(dat)[1:-1]) +';'
    curConn.execute(sql)
    dbConnect.commit()
    return 

def sqlDebug():
    dbConnect   = databaseOpen(database)
    curConn     = dbConnect.cursor()
    try:    
        sql     = "CREATE TABLE table_try (time);"
        curConn.execute(sql)
    except: pass
    sql         = "INSERT INTO table_try(time) values(12)"
    curConn.execute(sql)
    sql         = "SELECT * FROM table_try"
    curConn.execute(sql)
    print(curConn.fetchall())

    dbConnect.commit()
    curConn.close()
    databaseClose(dbConnect)

sqlDebug()