import matplotlib.pyplot as plt
from databaseProcess import *
from os import mkdir as pathMkdir
from os.path import exists as pathExists
imagePath = "sqlite3/image/"
dataDict = {'time':0, 'header':1, 'sysStatus':2, 'fyValue':3, 'fyAdStand':4, 
            'fyDistance':5, 'fyFlag':6, 'curTemp':7, 'jumpTemp':8, 'targetTemp':9, 
            'motoData':10, 'heatData':11, 'motoCur':12, 'remainTime':13, 
            'workedTime':14, 'endLine':15, 'id':16}
motoDataDict = {140:5, 10:10, 150:15, 130:130, 20:20, 160:25, 30:30, 170:35, 40:40, 180:45, 50:50,
                190:55, 60:60, 200:65, 70:70, 210:75, 80:80, 220:85, 90:90, 230:95, 100:100, 0:0}
heatDataDict = {91:5, 240:10, 101:15, 250:20, 111:25, 11:30, 121:35, 21:40, 131:45, 31:50, 141:55,
                41:60, 151:65, 51:70, 161:75, 61:80, 171:85, 71:90, 181:95, 81:100, 
                10:10, 20:20, 30:30, 40:40, 50:50, 60:60, 70:70, 80:80, 90:90, 100:100, 
                15:15, 25:25, 35:35, 45:45, 55:55, 65:65, 75:75, 85:85, 95:95, 0:0}
tableNames = [i[0] for i in                                 \
                sqlExe("SELECT name FROM sqlite_master      \
                        WHERE type='table' ORDER BY rowid") \
                    if i[0]!='sqlite_sequence']
def tableDatPlot(tableName):
    path = imagePath+tableName
    if not pathExists(path): pathMkdir(path)
    data = dbDataRead(tableName, list(dataDict.keys()))
    plt.figure(figsize=[6.4*2, 4.8*2])
    plt.plot(data[dataDict['workedTime']], data[dataDict['fyValue']], label='fyValue')
    plt.plot(data[dataDict['workedTime']], data[dataDict['fyAdStand']], label='fyAdStand')
    plt.plot(data[dataDict['workedTime']], data[dataDict['fyDistance']], label='fyDistance')
    plt.plot(data[dataDict['workedTime']], [i*100 for i in data[dataDict['fyFlag']]], label='fyFlag*100')
    plt.title('%s'%tableName)
    plt.xlabel('worked time/s')
    plt.ylabel('AD Value')
    plt.legend()
    plt.savefig(path+'/'+tableName+'_fy', dpi=500)

    plt.figure(figsize=[6.4*2, 4.8*2])
    plt.plot(data[dataDict['workedTime']], data[dataDict['curTemp']], label='curTemp')
    plt.plot(data[dataDict['workedTime']], data[dataDict['jumpTemp']], label='jumpTemp')
    plt.plot(data[dataDict['workedTime']], data[dataDict['targetTemp']], label='targetTemp')
    plt.title('%s'%tableName)
    plt.xlabel('worked time/s')
    plt.ylabel(u'Temp/℃')
    plt.legend()
    plt.savefig(path+'/'+tableName+'_Temp', dpi=500)

    plt.figure(figsize=[6.4*2, 4.8*2])
    plt.plot(data[dataDict['workedTime']], [motoDataDict[i] for i in data[dataDict['motoData']]], label='motoData')
    plt.plot(data[dataDict['workedTime']], [heatDataDict[i] for i in data[dataDict['heatData']]], label='heatData')
    plt.plot(data[dataDict['workedTime']], [i/300 for i in data[dataDict['motoCur']]], label='motoCur')
    plt.title('%s'%tableName)
    plt.xlabel('worked time/s')
    plt.ylabel(u'rank')
    plt.legend()
    plt.savefig(path+'/'+tableName+'_Data', dpi=500)

print(tableNames)
for tableName in tableNames:
    tableDatPlot(tableName)

# plt.show()
# print(sqlExe("SELECT id FROM %s"%(tableNames[-1])))
# print(tableNames)