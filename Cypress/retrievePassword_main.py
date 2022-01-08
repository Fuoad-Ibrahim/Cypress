from PyQt5 import QtCore, QtGui, QtWidgets
from database import database
from retrievePassword import RetrievePassword


class retrieveWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = RetrievePassword()
        self.ui.setupUi(self)

        self.ui.pushButtonRetrieve.clicked.connect(self.retrieve)
        #self.ui.pushButtonRetrieve.clicked.connect(self.cancel)

    def retrieve(self):

        username = self.ui.lineEditUsername.text()
        secretQuestion = self.ui.lineEditSecretQuestion.text()

        password = database.retrievePassword(username, secretQuestion)
        self.ui.label_3.setText(password)
        

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = retrieveWindow()
    widget.show()

    app.exec_()