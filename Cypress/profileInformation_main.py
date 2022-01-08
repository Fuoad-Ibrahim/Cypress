from profileInformation import Ui_Form
from database import database
import userDatabase
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QPushButton, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from password_strength import PasswordPolicy


class ProfileWindow(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.tableWidget_3.setColumnWidth(0, 110)
        self.ui.tableWidget_3.setColumnWidth(1, 110)
        self.ui.tableWidget_3.setColumnWidth(2, 270)
        self.ui.tableWidget_3.setColumnWidth(4, 200)
        self.ui.tableWidget_3.setColumnWidth(7, 380)
        self.loadinfo()

    def loadinfo(self):
        userinfo = userDatabase.getUserByUsername(database.getCurrentUser())

        self.ui.tableWidget_3.setRowCount(1)
        self.ui.tableWidget_3.setColumnCount(8)
        rows = 0
        for input in userinfo:
            self.ui.tableWidget_3.setItem(rows, 0, QtWidgets.QTableWidgetItem(input[0]))
            self.ui.tableWidget_3.setItem(rows, 1, QtWidgets.QTableWidgetItem(input[1]))
            self.ui.tableWidget_3.setItem(rows, 2, QtWidgets.QTableWidgetItem(input[2]))
            self.ui.tableWidget_3.setItem(rows, 3, QtWidgets.QTableWidgetItem(input[3]))
            self.ui.tableWidget_3.setItem(rows, 4, QtWidgets.QTableWidgetItem(input[4]))
            self.ui.tableWidget_3.setItem(rows, 5, QtWidgets.QTableWidgetItem(input[5]))
            self.ui.tableWidget_3.setItem(rows, 6, QtWidgets.QTableWidgetItem(input[6]))
            self.ui.tableWidget_3.setItem(rows, 7, QtWidgets.QTableWidgetItem(input[7]))
        rows+=1


    def updateInfo(self):

        firstname = self.ui.fnEdit_3.text()
        lastname = self.ui.lnEdit_3.text()
        address = self.ui.addressEdit_3.text()
        phonenumber = self.ui.phoneEdit_3.text()
        email = self.ui.emailEdit_3.text()
        password = self.ui.pwEdit_3.text()
        secretQuestion = self.ui.lineEdit_10.text()

        username = (database.getCurrentUser())

        #checks how many fields updated
        updated = 0

        if firstname != '':
            userDatabase.updatefirstname(firstname,username)
            updated += 1
        if lastname!= '':
            userDatabase.updatelastname(lastname,username)
            updated += 1
        if address!= '':
            userDatabase.updateaddress(address,username)
            updated += 1
        if phonenumber != '':
            userDatabase.updatephone(phonenumber,username)
            updated += 1
        if email != '':
            userDatabase.updateemail(email,username)
            updated += 1
        if password != '':
            userDatabase.updatepw(password, username)
            updated += 1
        if secretQuestion != '':
            userDatabase.updatesecretQ(secretQuestion, username)
            updated += 1

        if updated>0 :
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Profile info updated")
            msg.setWindowTitle("Success")
            msg.exec()







if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = ProfileWindow()
    widget.show()

    app.exec_()
