from PyQt5 import QtWidgets

from portalScreen import Ui_MainWindow
from reportingScreen_main import reportingScreen
from editReport_main import EditReportScreen
from tellFriend_main import TellFriend


class PortalWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #self.ui.pushButton.clicked.connect(self.navigate)

    def navigate(self):

        from reportingScreen_main import reportingScreen
        # Instantiate classes for all windows
        # portalWindow = PortalWindow()
        # reportingScreen = reportingScreen()
        # editReport = EditReportScreen()
        # tellFriend = TellFriend()
        #
        # # Adds windows to stack in order
        # widget.addWidget(portalWindow)
        # widget.addWidget(reportingScreen)
        # widget.addWidget(editReport)
        # widget.addWidget(tellFriend)

        # Navigates to "Tell a Friend" window
        if self.ui.radioButton_3.isChecked():
            widget.setCurrentIndex(1)
        elif self.ui.radioButton_8.isChecked():
            widget.setCurrentIndex(2)
        elif self.ui.radioButton_9.isChecked():
            widget.setCurrentIndex(3)

    def navigate_back(self):
        widget.setCurrentIndex(0)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    widget = QtWidgets.QStackedWidget()

    # Instantiate classes for all windows
    portalWindow = PortalWindow()
    reportingScreen = reportingScreen()
    editReport = EditReportScreen()
    tellFriend = TellFriend()

    # Adds windows to stack in order
    widget.addWidget(portalWindow)
    widget.addWidget(reportingScreen)
    widget.addWidget(editReport)
    widget.addWidget(tellFriend)

    # Sets fixed height and width for all windows in stack
    widget.setFixedHeight(600)
    widget.setFixedWidth(850)

    widget.show()

    app.exec_()

