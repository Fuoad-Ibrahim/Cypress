from deleteProfileFeedback import Ui_deleteProfileFeedback
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QPushButton, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from database import *



class FeedbackWindow(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_deleteProfileFeedback()
        self.ui.setupUi(self)
        self.ui.label_4.setText("1. Secret question for profile: What is your favourite colour? (case-sensitive)")

    def deleteProfile(self):
        answer = self.ui.lineEdit.text()

        if answer == database.retrievesecretQAnswer(database.getCurrentUser()):
            username = (database.getCurrentUser())

            confirmation = QMessageBox()
            promptbox = confirmation.question(self, '', "Are you sure you want to delete your profile and submitted reports?", confirmation.Yes | confirmation.No)

            if promptbox == confirmation.Yes:
                # The lines below are done in main.py
                # database.delete(username)
                # reportDatabase.deleteByUser(username)
                return True
            else:
                return False

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Answer incorrect")
            msg.setInformativeText("")
            msg.setWindowTitle("Error")
            msg.exec()
            return False


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = FeedbackWindow()
    widget.show()
    app.exec_()
