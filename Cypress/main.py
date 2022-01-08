#PyQt5 Tools
from PyQt5 import QtWidgets, QtGui, QtCore

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QPushButton, QMessageBox

# Databases
from database import database
import reportDatabase

# Windows
from mainScreen_main import mainScreen
from portalScreen_main import PortalWindow
from portalScreenLoggedin_main import PortalWindowLoggedIn
from loginScreen_main import loginWindow
from tellFriend_main import TellFriend
from faqscreen_main import faqscreen
from contact_main import contactus
from registrationScreen_main import registrationWindow
from profileInformation_main import ProfileWindow
from reportingScreen_main import reportingScreen
from editReport_main import EditReportScreen
from deleteProfileFeedback_main import FeedbackWindow
from retrievePassword_main import retrieveWindow
from adminScreen_main import adminScreen
from notificationScreen_main import notificationScreen
from rankingScreen_main import rankingScreen


class Main():
    def __init__(self):
        # Instantiates all windows
        self.mainScreen = mainScreen()
        self.portalWindow = PortalWindow()
        self.portalWindowLoggedIn = PortalWindowLoggedIn()
        self.loginWindow = loginWindow()
        self.tellFriend = TellFriend()
        self.faqScreen = faqscreen()
        self.stack = QtWidgets.QStackedWidget()
        self.contactUs = contactus()
        self.registrationWindow = registrationWindow()
        self.profileWindow = ProfileWindow()
        self.reportingScreen = reportingScreen()
        self.editReportScreen = EditReportScreen()
        self.feedBackWindow = FeedbackWindow()
        self.retrieveWindow = retrieveWindow()
        self.adminScreen = adminScreen()
        self.notificationScreen = notificationScreen()
        self.rankingScreen = rankingScreen()

        # Adds all windows to stack
        self.stack.addWidget(self.mainScreen)
        self.stack.addWidget(self.portalWindow)
        self.stack.addWidget(self.portalWindowLoggedIn)
        self.stack.addWidget(self.loginWindow)
        self.stack.addWidget(self.tellFriend)
        self.stack.addWidget(self.faqScreen)
        self.stack.addWidget(self.contactUs)
        self.stack.addWidget(self.registrationWindow)
        self.stack.addWidget(self.profileWindow)
        self.stack.addWidget(self.reportingScreen)
        self.stack.addWidget(self.editReportScreen)
        self.stack.addWidget(self.feedBackWindow)
        self.stack.addWidget(self.retrieveWindow)
        self.stack.addWidget(self.adminScreen)
        self.stack.addWidget(self.notificationScreen)
        self.stack.addWidget(self.rankingScreen)

        # Fix screen size
        self.stack.setFixedHeight(600)
        self.stack.setFixedWidth(850)

        # Redirection for mainScreen
        self.mainScreen.ui.pushButton.clicked.connect(lambda: self.redirect(self.portalWindow))

        # Redirection for portalScreen
        self.portalWindow.ui.pushButton.clicked.connect(self.redirect_portalWindow)

        # Redirection for tellFriend
        self.tellFriend.ui.pushButton_2.clicked.connect(self.redirect_to_loggedInPS_or_PS)

        # Redirection for contactUs
        self.contactUs.ui.pushButton.clicked.connect(self.redirect_to_loggedInPS_or_PS)

        # Redirection for faqScreen
        self.faqScreen.ui.pushButton.clicked.connect(self.redirect_to_loggedInPS_or_PS)

        # Redirection for loginWindow
        self.loginWindow.ui.pushButton.clicked.connect(self.redirect_loginWindow)
        self.loginWindow.ui.pushButton_2.clicked.connect(self.redirect_to_loggedInPS_or_PS)
        self.loginWindow.ui.pushButton_3.clicked.connect(lambda: self.redirect(self.retrieveWindow))

        # Redirection for retrievePassword
        self.retrieveWindow.ui.pushButton.clicked.connect(lambda: self.redirect(self.loginWindow))

        # Redirection for registrationWindow
        self.registrationWindow.ui.pushButton.clicked.connect(self.redirect_registrationWindow)
        self.registrationWindow.ui.pushButton_2.clicked.connect(lambda: self.redirect(self.portalWindow))

        # Redirection for portalWindowLoggedIn
        self.portalWindowLoggedIn.ui.pushButton.clicked.connect(self.redirect_portalWindowLoggedIn)
        self.portalWindowLoggedIn.ui.pushButton_2.clicked.connect(self.logout_and_redirect)
        self.portalWindowLoggedIn.ui.adminButton.clicked.connect(self.redirect_adminWindow)

        # Redirection for reportingScreen
        self.reportingScreen.ui.pushButton_2.clicked.connect(self.redirect_to_loggedInPS_or_PS)
        self.reportingScreen.ui.pushButton.clicked.connect(self.add_report)

        # Redirection for editReport
        self.editReportScreen.ui.cancelButton.clicked.connect(self.redirect_to_loggedInPS_or_PS)
        self.editReportScreen.ui.saveButton.clicked.connect(self.save_editReport)
        self.editReportScreen.ui.deleteReportButton.clicked.connect(self.delete_editReport)

        # Redirection for profileInformation
        self.profileWindow.ui.pushButton_5.clicked.connect(self.redirect_to_loggedInPS_or_PS)
        self.profileWindow.ui.pushButton_6.clicked.connect(self.redirect_to_loggedInPS_or_PS)
        self.profileWindow.ui.saveAndexit_3.clicked.connect(self.redirect_profileInformation)

        # Redirection for feedBackWindow
        self.feedBackWindow.ui.pushButton.clicked.connect(self.redirect_to_loggedInPS_or_PS)
        self.feedBackWindow.ui.pushButton_2.clicked.connect(self.redirect_feedBackWindow)

        # Redirection for adminScreen
        self.adminScreen.ui.backButton.clicked.connect(self.redirect_to_loggedInPS_or_PS)
        self.adminScreen.ui.resolveButton.clicked.connect(lambda: self.redirect(self.notificationScreen))
        self.adminScreen.ui.rankingButton.clicked.connect(lambda: self.redirect(self.rankingScreen))

        # Redirection for notificationScreen
        self.notificationScreen.ui.cancelButton.clicked.connect(lambda: self.redirect(self.adminScreen))

        # Redirection for rankingScreen
        self.rankingScreen.ui.doneButton.clicked.connect(lambda: self.redirect(self.adminScreen))

    def save_editReport(self):
        print('this is before save')
        print(reportDatabase.getReportsByUsername('bill'))
        self.editReportScreen.editReport()
        print('this is after after save')
        print(reportDatabase.getReportsByUsername('bill'))

        # Updates reports for editScreen
        self.editReportScreen.loadReportsDatabase()

        # Updates reporting screen for admin
        self.rankingScreen.loadAllProblems()
        self.rankingScreen.loadAllAddresses()

    def delete_editReport(self):
        print('this is before delete')
        print(reportDatabase.getReportsByUsername('bill'))
        self.editReportScreen.deleteReport()
        print('this is after delete')
        print(reportDatabase.getReportsByUsername('bill'))

        # Updates reports for editScreen
        #self.editReportScreen.loadReportsDatabase()

        # Updates reporting screen for admin
        self.rankingScreen.loadAllProblems()
        self.rankingScreen.loadAllAddresses()

    def logout_and_redirect(self):
        database.logout()
        self.stack.setCurrentWidget(self.portalWindow)

    def add_report(self):
        self.reportingScreen.reportIssue()

        # load report or editReport screen
        self.editReportScreen.loadReportsDatabase()

        # Updates reporting screen for admin
        self.rankingScreen.loadAllProblems()
        self.rankingScreen.loadAllAddresses()

    def redirect_profileInformation(self):
        self.profileWindow.updateInfo()
        self.stack.setCurrentWidget(self.portalWindowLoggedIn)

    def redirect_feedBackWindow(self):
        delete = self.feedBackWindow.deleteProfile()
        if delete is True:
            self.stack.setCurrentWidget(self.portalWindow)

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Profile and reports deleted")
            msg.setWindowTitle("Success")
            msg.exec()

            username = database.getCurrentUser()
            database.delete(username)
            reportDatabase.deleteByUser(username)


    def redirect(self, window):
        self.stack.setCurrentWidget(window)

    def redirect_to_PortalScreen(self):
        self.stack.setCurrentWidget(self.portalWindow)

    def redirect_to_loggedInPS_or_PS(self):
        user = database.getCurrentUser()
        # If user is logged in, go to portalWindowLoggedIn
        if database.isLoggedIn(user) is True:
            self.stack.setCurrentWidget(self.portalWindowLoggedIn)
        # If user is not logged in, go to portalWindow
        else:
            self.stack.setCurrentWidget(self.portalWindow)

    def redirect_portalWindowLoggedIn(self):
        # If "Profile info" is selected
        if self.portalWindowLoggedIn.ui.radioButton.isChecked():
            self.stack.setCurrentWidget(self.profileWindow)
            self.profileWindow.loadinfo()

        # If "Delete profile" is selected
        elif self.portalWindowLoggedIn.ui.radioButton_2.isChecked():
            self.stack.setCurrentWidget(self.feedBackWindow)

        # If "Report a Problem" is selected
        elif self.portalWindowLoggedIn.ui.radioButton_3.isChecked():
            self.stack.setCurrentWidget(self.reportingScreen)

        # If "Edit Report" is selected
        elif self.portalWindowLoggedIn.ui.radioButton_8.isChecked():
            self.editReportScreen.loadReportsDatabase()
            self.stack.setCurrentWidget(self.editReportScreen)

        # If "Tell a Friend" is selected
        elif self.portalWindowLoggedIn.ui.radioButton_9.isChecked():
            self.stack.setCurrentWidget(self.tellFriend)

        # If "FAQ" is selected
        elif self.portalWindowLoggedIn.ui.radioButton_6.isChecked():
            self.stack.setCurrentWidget(self.faqScreen)

        # If "Contact Us" is selected
        elif self.portalWindowLoggedIn.ui.radioButton_7.isChecked():
            self.stack.setCurrentWidget(self.contactUs)

    def redirect_portalWindow(self):
        # If "Register" is selected
        if self.portalWindow.ui.radioButton.isChecked():
            self.stack.setCurrentWidget(self.registrationWindow)
        # If "Login" is selected
        elif self.portalWindow.ui.radioButton_2.isChecked():
            self.stack.setCurrentWidget(self.loginWindow)
        # If "Tell a Friend" is selected
        elif self.portalWindow.ui.radioButton_9.isChecked():
            self.stack.setCurrentWidget(self.tellFriend)
        # If "FAQ" is selected
        elif self.portalWindow.ui.radioButton_6.isChecked():
            self.stack.setCurrentWidget(self.faqScreen)
        # If "Contact Us" is selected
        elif self.portalWindow.ui.radioButton_7.isChecked():
            self.stack.setCurrentWidget(self.contactUs)

    def redirect_loginWindow(self):
        if self.loginWindow.login() is True:
            self.stack.setCurrentWidget(self.portalWindowLoggedIn)

    def redirect_registrationWindow(self):
        if self.registrationWindow.registration() is True:
            self.stack.setCurrentWidget(self.loginWindow)
    
    def redirect_adminWindow(self):
        if database.getCurrentUser() == "admin":
            self.stack.setCurrentWidget(self.adminScreen)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    main = Main()
    main.stack.show()

    app.exec_()
