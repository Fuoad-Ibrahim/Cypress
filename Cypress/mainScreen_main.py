import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QPixmap, QIcon
from mainScreen import MainScreen

class mainScreen(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = MainScreen()
        self.ui.setupUi(self)

        #self.ui.pushButton.clicked.connect(self.click_English)
        self.ui.pushButton_2.clicked.connect(self.click_French)
    

    def click_English(self):
        print("English has been selected")
        
    def click_French(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("French option coming soon!!!")
        msg.setInformativeText("Stay tuned for more updates")
        msg.setWindowTitle("You selected Cypress in French")
        msg.exec()
        #print("French has been selected")
        

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = mainScreen()
    widget.show()

    app.exec_()