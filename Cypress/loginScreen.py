import sqlite3
import sys
from database import database
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QPushButton
from PyQt5.QtGui import QPixmap, QIcon

class LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 81, 31))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(630, 0, 161, 31))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 50, 761, 51))
        self.label_3.setScaledContents(True)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(470, 220, 93, 28))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(580, 220, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(460, 170, 111, 21))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(190, 170, 91, 21))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(190, 220, 91, 21))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(290, 170, 161, 31))
        self.lineEdit.setInputMask("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(290, 220, 161, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 30, 751, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(470, 270, 201, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        LoginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "LoginWindow"))
        self.label.setText(_translate("LoginWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Cypress</span></p></body></html>"))
        self.label_2.setText(_translate("LoginWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">City Of Toronto</span></p></body></html>"))
        self.label_3.setText(_translate("LoginWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">You are currently at the Cypress Login Page. By logging into this system, you will be able to report a variety of problems as you have witnessed on the streets of Toronto.</span></p></body></html>"))
        self.pushButton.setText(_translate("LoginWindow", "Login"))
        self.pushButton_2.setText(_translate("LoginWindow", "Cancel"))
        self.label_4.setText(_translate("LoginWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">@cypress.ca</span></p></body></html>"))
        self.label_5.setText(_translate("LoginWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Username:</span></p></body></html>"))
        self.label_6.setText(_translate("LoginWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Password:</span></p></body></html>"))
        self.pushButton_3.setText(_translate("MainWindow", "Forgot Password"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())


