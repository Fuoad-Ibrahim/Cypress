from contact import Ui_ContactUsWindow
from PyQt5 import QtCore, QtGui, QtWidgets


class contactus(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = Ui_ContactUsWindow()
        self.ui.setupUi(self)

        #self.ui.pushButton.clicked.connect(self.navigate_back)

    def navigate_back(self):
        widget.setCurrentIndex(1)


if __name__ == '__main__':
    from portalScreen_main import PortalWindow

    app = QtWidgets.QApplication([])

    widget = QtWidgets.QStackedWidget()

    # Instantiate classes
    contactus = contactus()
    portalScreen = PortalWindow()

    # Adds windows to stack in order
    widget.addWidget(contactus)
    widget.addWidget(portalScreen)

    # Sets fixed height and width for all windows in stack
    widget.setFixedHeight(600)
    widget.setFixedWidth(850)

    widget.show()

    app.exec_()