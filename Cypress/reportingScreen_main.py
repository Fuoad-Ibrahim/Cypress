from reportingScreen import Ui_ReportingWindow
import reportDatabase
import reportClass
from database import database

from PyQt5 import QtWidgets
from PyQt5 import QtCore


class reportingScreen(QtWidgets.QTabWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
        self.ui = Ui_ReportingWindow()
        self.ui.setupUi(self)

        #if Report is clicked:
        #self.ui.pushButton.clicked.connect(self.reportIssue)

        #if Cancel is clicked:
        #self.ui.pushButton_2.clicked.connect(self.gotomain) GO TO MAIN SCREEN
    
    def reportIssue(self):
        address = self.ui.lineEdit.text()
        issue = None

        #check which radio button is checked
        if self.ui.radioButton.isChecked():
            issue = self.ui.radioButton.text()
        elif self.ui.radioButton_2.isChecked():
            issue = self.ui.radioButton_2.text()
        elif self.ui.radioButton_3.isChecked():
            issue = self.ui.radioButton_3.text()
        elif self.ui.radioButton_4.isChecked():
            issue = self.ui.radioButton_4.text()
        elif self.ui.radioButton_5.isChecked():
            issue = self.ui.radioButton_5.text()
        elif self.ui.radioButton_6.isChecked():
            issue = self.ui.radioButton_6.text()
        elif self.ui.radioButton_7.isChecked():
            issue = self.ui.radioButton_7.text()
        elif self.ui.radioButton_8.isChecked():
            issue = self.ui.radioButton_8.text()
        
        if address == '' and issue == None:
            QtWidgets.QMessageBox.critical(self, 'Error', 'Please type in the address and select an issue')
        elif address == '':
            QtWidgets.QMessageBox.critical(self, 'Error', 'Please type in the address')
        elif issue == None:
            QtWidgets.QMessageBox.critical(self, 'Error', 'Please select an issue')
        else:
            #Create a confirmation window pop up
            confirmation = QtWidgets.QMessageBox()
            confirmation.setWindowTitle("Confirmation")
            confirmation.setIcon(QtWidgets.QMessageBox.Question)
            confirmationText = "Are you sure you want to submit the issue '" + issue + "' at the following address: " + address + "?"
            confirmation.setText(confirmationText)
            confirmation.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.Cancel)
            confirmation.setDefaultButton(QtWidgets.QMessageBox.Yes)
            #Add report to database
            submittedReport = reportClass.Report(database.getCurrentUser(), address, issue)
            reportDatabase.createNewReport(submittedReport)
            #confirmation.buttonClicked.connect(self.gotomain) GO TO MAIN SCREEN
            confirmation.exec_()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    widget = reportingScreen()
    widget.show()

    app.exec_()