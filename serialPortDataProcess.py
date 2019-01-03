from serial import Serial as serialSerial
from databaseProcess import *
from matPlotFromDb import *

# must be "postgre" or "sqlite3"
dbType          = "sqlite3"
serPort         = "COM5"
serPortBold     = 9600
serSize         = len(dataTypeName.split(','))+4
timeOut         = 1.5
UartRxLineHead  = 250
UartRxLineEnd   = 10

def uartDataProcess(ser):
    data = [i for i in ser.readline(serSize)]
    if(data == []): return []
    while len(data)<serSize: data = data + [i for i in ser.readline(serSize)]
    data =  data[:-9] +  \
            [   data[-9]*256+data[-8],
                data[-7]*3600+data[-6]*60+data[-5], 
                data[-4]*3600+data[-3]*60+data[-2],
                data[-1]  ]
    return data

def uartDbWrite(ser, dbConnect, tableName, dbType):
    curConn = dbConnect.cursor()
    data    = uartDataProcess(ser)
    writeCnt= 0
    while(data != []):
        if data[0]==UartRxLineHead and data[-1]==UartRxLineEnd and len(data)==len(dataTypeName.split(','))-1: 
            dbDataWrite(dbConnect, curConn, tableName, data, dbType)
            writeCnt = writeCnt + 1
            print("Write", dbType, "successfully:", data)
        data = uartDataProcess(ser)
    if writeCnt<30: 
        curConn.execute("DROP TABLE %s"%tableName)
        print("Drop table:", tableName, "successfully")
    else: tableDatPlot(tableName)
    dbConnect.commit()
    curConn.close()

def main():
    ser         = serialSerial(serPort, serPortBold, timeout=timeOut)
    dbConnect   = databaseOpen(database, user, password, dbType)
    
    for tableName in tableNames: 
        if sqlExe("SELECT id FROM %s"%(tableName))==[]: dbTableDelete([tableName])
    try: 
        while 1: 
            tableName = dbTableCreate(dbConnect, dataType)
            uartDbWrite(ser, dbConnect, tableName, dbType)
    except  KeyboardInterrupt:
        if sqlExe("SELECT id FROM %s"%(tableName))==[]: dbTableDelete([tableName])
    databaseClose(dbConnect, dbType)
    ser.close()

main()