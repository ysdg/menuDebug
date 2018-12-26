from serial import Serial as serialSerial
import serial.tools.list_ports
from databaseProcess import *

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

ser = serialSerial(serPort, serPortBold, timeout=timeOut)

dbConnect   = databaseOpen(database, user, password)
tableName   = dbTableCreate(dbConnect, dataType)
curConn     = dbConnect.cursor()

data = uartDataProcess(ser)
while(data != []):
    if data[0]==UartRxLineHead and data[-1]==UartRxLineEnd and len(data)==len(dataTypeName.split(','))-1: 
        dbDataWrite(dbConnect, curConn, tableName, data)
        print("Write db successfully", data)
    data = uartDataProcess(ser)

curConn.close()
databaseClose(dbConnect)

ser.close()