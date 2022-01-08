import sqlite3
import sys
from database import database
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QPushButton, QMessageBox
from PyQt5.QtGui import QPixmap, QIcon
from loginScreen import LoginWindow


class loginWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = LoginWindow()
        self.ui.setupUi(self)

    def login(self):
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()

        if database.login(username, password):
            # print("Username correct!")
            # print("Password correct!")
            # print("Logging in...")
            return True
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Please Try Again")
            msg.setInformativeText("Username/Password Incorrect")
            msg.setWindowTitle("Login Error")
            msg.exec()
            # print("Something wrong")
            return False


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = loginWindow()
    widget.show()

    app.exec_()
