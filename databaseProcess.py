import psycopg2

# absolute time
from datetime import datetime
time = datetime.now()

database    = "test"
user        = "yuanquan"
password    = "yuanquan"

def dbTableInfoInput():
    print("Please input menu:")
    str = input()
    print("Please materials(g):")
    str = str+'_'+input()+'g'
    print("Please water level(ml):")
    str = str+'_'+input()+'ml'+'_'+datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    return str


def dbTableCreate(database, user, password):
    dbConnect   = psycopg2.connect(database=database, user=user, password=password)
    print("Opened database", database, "successfully")
    curConn     = dbConnect.cursor()
    data        =   """
                    id  bigint  NOT NULL,
                    time timestamp NOT NULL, 
                    header int NOT NULL,
                    fy int NOT NULL
                    """
    dbName = dbTableInfoInput()
    sql     = "CREATE TABLE T%s (%s)"%(dbName, data)+';'
    curConn.execute(sql)
    dbConnect.commit()
    curConn.close()
    dbConnect.close()
    return dbName

def dbDataWrite(dbConnect, dat):
    curConn     = dbConnect.cursor()
    curConn.execute("""
                    ALTER TABLE %s 
                    """)
    dbConnect.commit()
    curConn.close()
    dbConnect.close()
    return

# dbTableCreate()
# print(dbTableInfoInput())
dbTableCreate(database, user, password)