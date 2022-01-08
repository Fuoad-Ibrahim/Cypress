from secretqPrompt1 import Ui_secretQPrompt
import userDatabase
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QPushButton, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from database import database


class secretQWindow(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_secretQPrompt()
        self.ui.setupUi(self)

        self.ui.pushButton_2.clicked.connect(self.confirmSecretQ)

    def confirmSecretQ(self):

        answer = self.ui.lineEdit.text()

        if answer == database.retrievesecretQAnswer(database.getCurrentUser()):
            confirmation = QtWidgets.QMessageBox()
            confirmation.setWindowTitle("Confirmation")
            confirmation.setIcon(QtWidgets.QMessageBox.Question)
            confirmationText = "Are you sure you want to delete this profile and all submitted reports?"
            confirmation.setText(confirmationText)
            confirmation.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            confirmation.setDefaultButton(QtWidgets.QMessageBox.Yes)
            confirmation.exec_()
            
                #redirect confirmation qMessageBox prompt "yes" to deleteprofile
            
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Answer incorrect")
            msg.setInformativeText("")
            msg.setWindowTitle("Error")
            msg.exec()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = secretQWindow()
    widget.show()
    app.exec_()
