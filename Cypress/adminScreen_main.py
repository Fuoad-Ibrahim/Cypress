from adminScreen import Ui_Admin
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class adminScreen(QMainWindow):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.ui = Ui_Admin()
		self.ui.setupUi(self)


if __name__ == '__main__':
	app = QtWidgets.QApplication([])
	widget = adminScreen()
	widget.show()
	
	app.exec_()