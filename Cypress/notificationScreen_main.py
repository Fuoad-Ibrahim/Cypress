from notificationScreen import Ui_Notification
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class notificationScreen(QMainWindow):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.ui = Ui_Notification()
		self.ui.setupUi(self)

		self.ui.label_2.setText("Message")

		self.ui.sendButton.clicked.connect(self.sentPressed)

	def getText(self):
		return self.ui.textBox.toPlainText()

	def sentPressed(self):
		self.check_sendNotification()
		x = self.ui.userBox.isChecked()
		y = self.ui.cityBox.isChecked()
		popup = QtWidgets.QMessageBox()
		message = self.getText()
		if x:
			if message == "":
				message = "No message"
				popup.setWindowTitle("ERROR")
				popup.setText(message)
				popup.exec_()
			else:
				popup.setWindowTitle("Confirmation")
				popup.setText("Sent Message to Users: '" + message + "'")
				popup.exec_()
		elif y:
			if message == "":
				message = "No message"
				popup.setWindowTitle("ERROR")
				popup.setText(message)
				popup.exec_()
			else:
				popup.setWindowTitle("Confirmation")
				popup.setText("Sent Message to City Officials: '" + message + "'")
				popup.exec_()
		else:
			message = "No recipient selected"
			popup.setWindowTitle("ERROR")
			popup.setText(message)
			popup.exec_()

	def check_sendNotification(self):
			message = self.getText()
			x = self.ui.userBox.isChecked()
			y = self.ui.cityBox.isChecked()
			if (x or y) and (not message == ""):
				return True
			else:
				return False 

if __name__ == '__main__':
	app = QtWidgets.QApplication([])
	widget = notificationScreen()
	widget.show()
	
	app.exec_()