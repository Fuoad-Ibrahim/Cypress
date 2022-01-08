from rankingScreen import Ui_Ranking
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
import sqlite3

conn = sqlite3.connect('reports.db')
c = conn.cursor()


class rankingScreen(QDialog):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.ui = Ui_Ranking()
		self.ui.setupUi(self)
		
		self.loadAllProblems()
		self.loadAllAddresses()

	def loadAllProblems(self):
		self.ui.rankedList.clear()
		counter = [0, 0, 0, 0, 0, 0, 0, 0]
		allreports = self.getAllReports()
		for report in allreports:
			if report[3] == "Utility Failures":
				counter[0] = counter[0]+1
			elif report[3] == "Potholes":
				counter[1] = counter[1]+1
			elif report[3] == "City Property Vandalism":
				counter[2] = counter[2]+1
			elif report[3] == "Eroded Streets":
				counter[3] = counter[3]+1
			elif report[3] == "Tree Collapse":
				counter[4] = counter[4]+1
			elif report[3] == "Flooded Streets":
				counter[5] = counter[5]+1
			elif report[3] == "Mold and Spore Growth":
				counter[6] = counter[6]+1
			elif report[3] == "Garbage or Any Other Road Blocking":
				counter[7] = counter[7]+1
		problemList = ["Utility Failures","Potholes","City Property Vandalism","Eroded Streets","Tree Collapse","Flooded Streets","Mold and Spore Growth","Garbage or Any Other Road Blocking"]
		for i in range(0, 8):
			counter[i] = [counter[i], problemList[i]]
		counter.sort()
		for i in reversed(counter):
			self.ui.rankedList.append(i[1] + " (" + str(i[0]) + " reports)")
		return True

	def loadAllAddresses(self):
		self.ui.addressList.clear()
		counter = []
		addresses = []
		addwithdupe = []
		allreports = self.getAllReports()
		for report in allreports:
			cur = ''.join([i for i in report[2] if not i.isdigit()])
			addwithdupe.append(cur)
		for i in addwithdupe:
			if i not in addresses:
				addresses.append(i)
		for i in range(0, len(addresses)):
			counter.append([0, addresses[i]])
		for i in addwithdupe:
			for f in counter:
				if i == f[1]:
					f[0] = f[0]+1
		counter.sort()
		for i in reversed(counter):
			self.ui.addressList.append(i[1] + " (" + str(i[0]) + " reports)")
		return True

	def getAllReports(self):
		return c.execute("SELECT * FROM reports")

	
	
if __name__ == '__main__':
	app = QtWidgets.QApplication([])

	widget = rankingScreen()
	widget.show()

	app.exec_()