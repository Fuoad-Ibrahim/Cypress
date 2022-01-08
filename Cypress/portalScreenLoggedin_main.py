from PyQt5 import QtWidgets

from portalScreenLoggedin import Ui_MainWindow
from tellFriend_main import TellFriend


class PortalWindowLoggedIn(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.stack = QtWidgets.QStackedWidget()
        self.stack.addWidget(self)
        self.stack.addWidget(TellFriend())
        self.stack.setFixedHeight(600)
        self.stack.setFixedWidth(850)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    win = PortalWindowLoggedIn()
    win.stack.show()
    app.exec_()