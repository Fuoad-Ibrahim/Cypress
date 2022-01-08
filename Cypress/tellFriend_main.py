from tellFriend import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets


class TellFriend(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #self.ui.pushButton_2.clicked.connect(self.navigate_back)
        self.ui.pushButton.clicked.connect(self.sendmessage)
    
    def navigate_back(self):
        stack = QtWidgets.QStackedWidget()
        stack.addWidget(portalScreenLoggedin_main.PortalWindow())
        stack.setFixedHeight(600)
        stack.setFixedWidth(850)
        stack.show()

    def sendmessage(self):
        email = self.ui.lineEdit.text()
        
        if email != "":
            if "@" in email:
                #Create a confirmation window pop up
                success = QtWidgets.QMessageBox()
                success.setWindowTitle("Success")
                success.setIcon(QtWidgets.QMessageBox.Information)
                successText = "Your message was sent to " + email
                success.setText(successText)
                success.setStandardButtons(QtWidgets.QMessageBox.Ok)
                success.setDefaultButton(QtWidgets.QMessageBox.Ok)
                success.exec_()
            else:
                QtWidgets.QMessageBox.critical(self, 'Error', 'Email must contain @')
        else:
            QtWidgets.QMessageBox.critical(self, 'Error', 'Please type in the email')


    # def navigate_back(self):
    #     from portalScreen_main import PortalWindow
    #     a = QtWidgets.QApplication([])
    #
    #     p = PortalWindow()
    #     p.show()
    #
    #     a.exec_()
    #     #widget.setCurrentIndex(1)
    #     #p = PortalWindow()
    #     #p.navigate_back()

if __name__ == '__main__':
    #from portalScreen_main import PortalWindow

    app = QtWidgets.QApplication([])

    widget = QtWidgets.QStackedWidget()

    # Instantiate classes
    tellFriend = TellFriend()
    #portalScreen = PortalWindow()

    # Adds windows to stack in order
    widget.addWidget(tellFriend)
    #widget.addWidget(portalScreen)

    # Sets fixed height and width for all windows in stack
    widget.setFixedHeight(600)
    widget.setFixedWidth(850)

    widget.show()

    app.exec_()

