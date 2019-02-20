from psycopg2 import connect as psycopg2Connect
from sqlite3 import connect as sqlite3Connect

# absolute time
from datetime import datetime
time = datetime.now()

# only for sqlite3 database
databasePath= "../sqlite3/database/"
# "default" or "input", default: soyMilk, 140g, 1400ml
menuMsg     = "input"
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

def sqlExe(sql, database=database, user=user, password=password, dbType='sqlite3'):
    dbConnect = databaseOpen(database, user, password, dbType)
    curConn   = dbConnect.cursor()
    curConn.execute(sql)
    data      = curConn.fetchall()
    dbConnect.commit()
    databaseClose(dbConnect, dbType)
    return data

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
    sql = "SELECT * FROM sqlite_master WHERE type='table' ORDER BY rowid"
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
# print(sqlExe("SELECT name FROM sqlite_master      \
#                 WHERE type='table' and rowid=(SELECT MAX(rowid) FROM sqlite_master)")[0][0])