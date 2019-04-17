# !/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from databaseProcess import *
from os import mkdir as pathMkdir
from os.path import exists as pathExists

# tableNames = [i[0] for i in                                 \
# 				sqlExe("SELECT name FROM sqlite_master      \
# 						WHERE type='table' ORDER BY rowid") \
# 					if i[0]!='sqlite_sequence']

dataDict = {'time':0, 'header':1, 'sysStatus':2, 'fyValue':3, 'fyAdStand':4, 
			'fyDistance':5, 'fyFlag':6, 'curTemp':7, 'jumpTemp':8, 'targetTemp':9, 
			'motoData':10, 'heatData':11, 'motoCur':12, 'endLine':13, 'id':14}
motoDataDict = {140:5, 10:10, 150:15, 130:130, 20:20, 160:25, 30:30, 170:35, 40:40, 180:45, 50:50,
				190:55, 60:60, 200:65, 70:70, 210:75, 80:80, 220:85, 90:90, 230:95, 100:100, 0:0}
heatDataDict = {91:5, 240:10, 101:15, 250:20, 111:25, 11:30, 121:35, 21:40, 131:45, 31:50, 141:55,
				41:60, 151:65, 51:70, 161:75, 61:80, 171:85, 71:90, 181:95, 81:100, 
				10:10, 20:20, 30:30, 40:40, 50:50, 60:60, 70:70, 80:80, 90:90, 100:100, 
				15:15, 25:25, 35:35, 45:45, 55:55, 65:65, 75:75, 85:85, 95:95, 0:0}

class DataToPlot():
	def __init__(self, dat=[], xclo="", yclos=[], rows=[], xlabel="", ylable="", title="", labels=[]):
		""" 
		dat: data to plot;
		xclo: the x cloumns to plot, should only once;
		yclos: the y cloumns to plot, can be more than one, default by all;
		rows: the rows limit to plot, default by all;
		xlabel, ylabel: x and y label for uint;
		title: title for the plot name;
		labels: every plot line name, should be cloumns;
		figsize, figdpi: not input, but be setted here;
		imagePath: path to store the image.
		 """
		self.dat = dat
		if xclo==[]: 
			print(self+"x cloumn has no data!")
			exit()
		else: self.xclo = xclo
		if yclos==[]: 
			if dat!=[]: self.yclos = [i for i in range(len(dat[0]))]
			else: 
				print(str(self)+".yclos need input!")
				self.yclos = []
		else: self.yclos = yclos
		self.yclos = yclos
		self.rows = rows
		self.xlabel = xlabel
		self.ylabel = ylable
		self.title = title
		if labels == []: self.labels = self.yclos
		else: self.labels = labels
		self.figsize = [6.4*2, 4.8*2]
		self.figdpi = 500
		self.imagePath = "./document/image/"
	def plot(self):
		""" plot based on dataDict, motoDataDict, heatDataDict """
		path = self.imagePath + self.title +datetime.now().strftime('%Y%m%d_%H%M%S')
		if not pathExists(path): pathMkdir(path)	
		plt.figure(figsize=self.figsize)
		plt.title(self.title)
		plt.xlabel(self.xlabel)
		plt.ylabel(self.ylabel)
		for yclo in self.yclos:
			xDat = self.dat[dataDict[self.xclo]]
			if yclo=='motoData': yDat = [motoDataDict[i] for i in self.dat[dataDict[yclo]]]
			elif yclo=='heatData': yDat = [heatDataDict[i] for i in self.dat[dataDict[yclo]]]
			else: yDat = self.dat[dataDict[yclo]]
			plt.plot(xDat, yDat, label=yclo)
		plt.legend()
		plt.savefig(path+'/'+self.title, dpi=self.figdpi)
	def dataReadFromTable(self, tablename, dbType="postgre"):
		self.dat = dbDataRead(tablename, list(dataDict.keys()), dbType)
	def dataPlotFromTables(self, tablenames=[], dbType="postgre"):
		""" 
		plot date from table names and plot to a picture
		tablenames: table name to data
		dbType: database type, default by postgre
		 """
		path = self.imagePath + self.title +datetime.now().strftime('%Y%m%d_%H%M%S')
		if not pathExists(path): pathMkdir(path)
		plt.figure(figsize=self.figsize)
		plt.title(self.title)
		plt.xlabel(self.xlabel)
		plt.ylabel(self.ylabel)
		for tablename in tablenames:
			self.dataReadFromTable(tablename)
			for yclo in self.yclos:
				plt.plot(self.dat[dataDict[self.xclo]], self.dat[dataDict[yclo]], label=tablename)
		plt.legend()
		plt.savefig(path+'/'+self.title, dpi=self.figdpi)

if __name__ == "__main__":
	datToPlot = DataToPlot(xclo="id")
	datToPlot.title = "test"
	datToPlot.yclos = ["motoCur"]
	datToPlot.xlabel = "work time /100ms"
	datToPlot.ylabel = "moto current AD value"
	tableNames = ["t_motol10_water_1400ml_2019_03_21_09_41_23", "t_motol10_water_1500ml_2019_03_21_09_43_17", "t_motol10_water_1600ml_2019_03_21_09_44_45"]
	datToPlot.dataPlotFromTables(tableNames)
	# datToPlot.plot()
	pass


# print(tableNames)
# for tableName in tableNames:
#     tableDatPlot(tableName)

# plt.show()
# print(sqlExe("SELECT id FROM %s"%(tableNames[-1])))
# print(tableNames)