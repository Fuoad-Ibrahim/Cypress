from faqscreen import Ui_FaqWindow
from PyQt5 import QtCore, QtGui, QtWidgets


class faqscreen(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = Ui_FaqWindow()
        self.ui.setupUi(self)


if __name__ == '__main__':
    from portalScreen_main import PortalWindow

    app = QtWidgets.QApplication([])

    widget = QtWidgets.QStackedWidget()

    # Instantiate classes
    faqscreen = faqscreen()
    portalScreen = PortalWindow()

    # Adds windows to stack in order
    widget.addWidget(faqscreen)
    widget.addWidget(portalScreen)

    # Sets fixed height and width for all windows in stack
    widget.setFixedHeight(620)
    widget.setFixedWidth(800)

    widget.show()

    app.exec_()