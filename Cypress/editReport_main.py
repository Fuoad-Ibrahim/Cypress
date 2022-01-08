from editReport import Ui_MainWindow
import reportDatabase
import reportClass
from database import database

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *


class EditReportScreen(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.tableWidget.setColumnCount(3)
        self.ui.tableWidget.setColumnWidth(0, 100)
        self.ui.tableWidget.setColumnWidth(1, 259)
        self.ui.tableWidget.setColumnWidth(2, 258)
        self.ui.tableWidget.setHorizontalHeaderLabels(["Report number", "Address", "Issue"])

        self.loadReportsDatabase()

        #if Save is clicked:
        #self.ui.saveButton.clicked.connect(self.editReport)

        #if Cancel is clicked: ---> take to home page without saving
        
        #if Delete report is clicked:
        #self.ui.deleteReportButton.clicked.connect(self.deleteReport)

    def loadReportsDatabase(self):
        row = 0

        listofreports = reportDatabase.getReportsByUsername(database.getCurrentUser())

        self.ui.tableWidget.setRowCount(5)
        if len(listofreports) != 0:
            self.ui.tableWidget.clear()
            for report in listofreports:
                print(report[0])
                print('editReport -- load Reports')
                self.ui.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(report[0])))
                self.ui.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(report[2]))
                self.ui.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(report[3]))
                row += 1
        else:
            self.ui.tableWidget.clear()

    def editReport(self):
        reportNumber = self.ui.selectedReport.text()

        newaddress = self.ui.newAddressLine.text()
        newissue = None

        if reportNumber != "":
            if self.ui.radioButton.isChecked():
                newissue = self.ui.radioButton.text()
            elif self.ui.radioButton_2.isChecked():
                newissue = self.ui.radioButton_2.text()
            elif self.ui.radioButton_3.isChecked():
                newissue = self.ui.radioButton_3.text()
            elif self.ui.radioButton_4.isChecked():
                newissue = self.ui.radioButton_4.text()
            elif self.ui.radioButton_5.isChecked():
                newissue = self.ui.radioButton_5.text()
            elif self.ui.radioButton_6.isChecked():
                newissue = self.ui.radioButton_6.text()
            elif self.ui.radioButton_7.isChecked():
                newissue = self.ui.radioButton_7.text()
            elif self.ui.radioButton_8.isChecked():
                newissue = self.ui.radioButton_8.text()
            
            if newaddress == '' and newissue == None:
                QtWidgets.QMessageBox.critical(self, 'Error', 'Please type in a new address or select a new issue (or both)')
            else:
                #Create a confirmation window pop up
                success = QtWidgets.QMessageBox()
                success.setWindowTitle("Success")
                success.setIcon(QtWidgets.QMessageBox.Information)
                successText = "Report number " + reportNumber + " was successfully updated"
                success.setText(successText)
                success.setStandardButtons(QtWidgets.QMessageBox.Ok)
                success.setDefaultButton(QtWidgets.QMessageBox.Ok)
                
                if newaddress != '' and newissue != None:
                    reportDatabase.updateIssue(reportNumber, newissue)
                    reportDatabase.updateAddress(reportNumber, newaddress)
                    success.exec_()
                    self.loadReportsDatabase()
                elif newaddress != '' and newissue == None:
                    reportDatabase.updateAddress(reportNumber, newaddress)
                    success.exec_()
                    self.loadReportsDatabase()
                elif newaddress == '' and newissue != None:
                    reportDatabase.updateIssue(reportNumber, newissue)
                    success.exec_()
                    self.loadReportsDatabase()
        else:
            QtWidgets.QMessageBox.critical(self, 'Error', 'Please type in report number')

    def deleteReport(self):
        reportNumber = self.ui.selectedReport.text()
        if reportNumber != "":
            confirmation = QtWidgets.QMessageBox()
            confirmation.setWindowTitle("Confirmation")
            confirmation.setIcon(QtWidgets.QMessageBox.Question)
            confirmationText = "Are you sure you want to delete report number " + reportNumber + "?"
            confirmation.setText(confirmationText)
            confirmation.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.Cancel)
            confirmation.setDefaultButton(QtWidgets.QMessageBox.Yes)
            
            if confirmation.exec_() == QtWidgets.QMessageBox.Yes:
                reportDatabase.deleteReport(reportNumber)
                self.loadReportsDatabase()
        else:
            QtWidgets.QMessageBox.critical(self, 'Error', 'Please type in report number')


if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    widget = EditReportScreen()
    widget.show()

    app.exec_()