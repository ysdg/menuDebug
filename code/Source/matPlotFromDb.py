# !/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from databaseProcess import *
from os import mkdir as pathMkdir
from os.path import exists as pathExists
import numpy as np

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
	""" 
	class to plot data based on matplotlib
	 """
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
		imagePath: path to store the image;
		dbOperation: DB operater, connection for data importing.
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
		self.labels = labels
		self.figsize = [6.4*2, 4.8*2]
		self.figdpi = 500
		self.imagePath = "./document/image/"
		self.dbOperation = databaseOperation()

	def plot(self):
		""" 
		plot based on dataDict, motoDataDict, heatDataDict
		 """
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

	def dataReadFromTable(self, tablename):
		""" 
		read all data from tablename by cols.
		 """
		self.dat = self.dbOperation.dbDataRead(tablename, list(dataDict))

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
	def plotOnePicture(self, xDats, yDats):
		""" 
		plot x, y data to one picture;
		label, title and so on is based on the class;
		xDats, yDats: x, y data, must be list and corrosspondly
		 """
		path = self.imagePath + self.title +datetime.now().strftime('%Y%m%d_%H%M%S')
		if not pathExists(path): pathMkdir(path)
		plt.figure(figsize=self.figsize)
		plt.title(self.title)
		plt.xlabel(self.xlabel)
		plt.ylabel(self.ylabel)
		for xDat, yDat, label in zip(xDats, yDats, self.labels):
			plt.plot(xDat, yDat, label=label)
		plt.legend()
		plt.savefig(path+'/'+self.title, dpi=self.figdpi)
	def datProcess(self, tablenames):
		self.rows = [100, 150]
		yDats = []
		xDats = []
		for i,tablename in enumerate(tablenames):
			self.dataReadFromTable(tablename)
			dataCur = self.dat[dataDict["motoCur"]][self.rows[0]:self.rows[1]]
			dataId = self.dat[dataDict["id"]][self.rows[0]:self.rows[1]]
			yTmp, xTmp=self.topFilter(dataCur, dataId)
			xDats.append(xTmp)
			yDats.append(yTmp)
			self.labels[i] = tablename.split("_")[2]+'-'+tablename.split("_")[3] +":{:.1f}".format(self.meanFilter(yTmp))
		self.plotOnePicture(xDats, yDats)
	def topFilter(self, datas, dataId=[]):
		dataTmp = []
		if dataId != []: dataIdTmp=[]
		for i in range(len(datas)-1):
			if datas[i]>datas[i-1] and datas[i]>datas[i+1]:
				dataTmp.append(datas[i])
				if dataId!=[]: dataIdTmp.append(dataId[i])
		if dataId != []: return dataTmp, dataIdTmp
		else: return dataTmp
	def outValleyFilter(self, datas, dataId=[]):
		dataTmp = []
		if dataId != []: dataIdTmp=[]
		for i in range(len(datas)-1):
			if datas[i]>datas[i-1] or datas[i]>datas[i+1]:
				dataTmp.append(datas[i])
				if dataId!=[]: dataIdTmp.append(dataId[i])
		if dataId != []: return dataTmp, dataIdTmp
		else: return dataTmp
	def meanFilter(self, datas):
		datasTmp = datas[:]
		maxDat = datasTmp[0]
		minDat = datasTmp[0]
		for dat in datasTmp:
			if dat > maxDat: maxDat = dat
			if dat < minDat: minDat = dat
		datasTmp.remove(maxDat)
		datasTmp.remove(minDat)
		return np.mean(datasTmp)
	def datFliterProcess(self, tablenames):
		self.rows = [1, 150]
		# xDats,yDats,xTmpTop,yTmpTop,xTmpValley,yTmpValley,xTmpMean,yTmpMean=[],[],[],[],[],[],[],[]
		xDats, yDats, xTmpValley, yTmpValley = [], [], [], []
		for tablename in tablenames:
			self.dataReadFromTable(tablename)
			dataCur = self.dat[dataDict["motoCur"]][self.rows[0]:self.rows[1]]
			dataId = self.dat[dataDict["id"]][self.rows[0]:self.rows[1]]
			# yTmpTop.append(self.meanFilter(self.topFilter(dataCur)))
			# xTmpTop.append(self.meanFilter(self.topFilter(dataId)))
			# yTmpValley.append(self.meanFilter(self.outValleyFilter(dataCur)))
			# xTmpValley.append(self.meanFilter(self.outValleyFilter(dataId)))
			yTmpValley, xTmpValley = self.outValleyFilter(dataCur, dataId)
			xDats.append(xTmpValley), yDats.append(yTmpValley)
			# xTmpValley.append(int(tablename.split("_")[3][:-2]))
			# yTmpMean.append(self.meanFilter(dataCur))
			# xTmpMean.append(int(tablename.split("_")[3][:-2]))
		# self.labels.append("no fileter mean"), xDats.append(xTmpMean), yDats.append(yTmpMean)
		# self.labels.append("top fileter mean"), xDats.append(xTmpTop), yDats.append(yTmpTop)
		# self.labels.append("out Valley fileter mean"), xDats.append(xTmpValley), yDats.append(yTmpValley)
		# self.labels.append("out Valley fileter mean")
		self.plotOnePicture(xDats, yDats)
		# print(xDats, yDats)


if __name__ == "__main__":
	datToPlot = DataToPlot(xclo="id")
	datToPlot.dbOperation.databaseOpen()
	datToPlot.title = "moto rank--current"
	datToPlot.yclos = ["motoCur"]
	datToPlot.xlabel = "work time /100ms"
	datToPlot.ylabel = "moto current AD value"
	datToPlot.labels = ["water-motoL5", "juice-motoL5", "nut-motoL5", \
						"water-motoL10", "juice-motoL10", "nut-motoL10"]
	tableNames = [	"t_motol10_water_700ml_2019_03_25_13_47_51",	\
					"t_motol10_water_900ml_2019_03_25_13_51_21",	\
					"t_motol10_water_1100ml_2019_03_25_13_54_34", 	\
					"t_motol10_water_1300ml_2019_03_25_13_57_31", 	\
					"t_motol10_water_1500ml_2019_03_25_14_01_01", 	\
					"t_motol10_water_1750ml_2019_03_25_14_04_11"]
	datToPlot.datFliterProcess(tableNames)
	datToPlot.dbOperation.databaseClose()
	pass