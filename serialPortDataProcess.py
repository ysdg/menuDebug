from serial import Serial as serialSerial

serPort = "COM6"
serPortBold = 9600
serSize = 20
timeOut = 500
# def serReadProcess(Size, ser):
#     if ser.read(2) == int('0xFA', 16)：

ser = serialSerial(serPort, serPortBold)
ser.read(serSize)

ser.close()