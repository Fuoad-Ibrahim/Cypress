import sys
from database import database
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QPushButton, QMessageBox
from PyQt5.QtGui import QPixmap, QIcon
from password_strength import PasswordPolicy
from registrationScreen import RegistrationWindow

class registrationWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = RegistrationWindow()
        self.ui.setupUi(self)


    def registration(self):

        policy = PasswordPolicy.from_names(
        length=8,  # min length: 8
        uppercase=2,  # need min. 2 uppercase letters
        numbers=2,  # need min. 2 digits
        special=2,  # need min. 2 special characters
        nonletters=2,  # need min. 2 non-letter characters (digits, specials, anything)
        )

        firstname = self.ui.lineEdit_6.text()
        lastname = self.ui.lineEdit.text()  
        address = self.ui.lineEdit_2.text()
        phonenumber = self.ui.lineEdit_3.text()
        email = self.ui.lineEdit_4.text()       
        username = self.ui.lineEdit_7.text()
        password  = self.ui.lineEdit_8.text()
        secretQuestion  = self.ui.lineEdit_5.text()

        if firstname == '':
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Please enter your first name")
            msg.setInformativeText("First name field cannot be left empty")
            msg.setWindowTitle("Missing First Name")
            msg.exec()
            return False
        if lastname == '' :
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Please enter your last name")
            msg.setInformativeText("Last name field cannot be left empty")
            msg.setWindowTitle("Missing Last Name")
            msg.exec()
            return False
        if len(address) < 10:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Please enter a valid address")
            msg.setInformativeText("Addresses should include Street No., Street, City, Province, Postal Code, Country")
            msg.setWindowTitle("Missing or Invalid Address")
            msg.exec()
            return False
        if len(phonenumber) > 13 or len(phonenumber) < 10: 
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Please enter a valid phone number")
            msg.setInformativeText("Phone number must be between 10 to 13 characters of format 416-XXX-XXX or 416XXXXXXX")
            msg.setWindowTitle("Missing or Invalid Phone Number")
            msg.exec()
            return False
        if len(email) < 8:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Please enter a valid email address")
            msg.setInformativeText("Please include @cypress.ca")
            msg.setWindowTitle("Missing or invalid email")
            msg.exec()
            return False
        if username == '':
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Please enter a username")
            msg.setInformativeText("Username field cannot be left empty")
            msg.setWindowTitle("Missing username")
            msg.exec()
            return False
        if username == '':
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Please enter new username")
            #msg.setInformativeText("Username field needs to be unique")
            msg.setWindowTitle("Enter unique username")
            msg.exec()
            return False
        if len(secretQuestion) < 2:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Please enter a valid answer to the secret question")
            msg.setInformativeText("Answer to secret question cannot be left blank")
            msg.setWindowTitle("Missing or Invalid Answer to Secret Question")
            msg.exec()  
            return False


        if len(policy.test(password)) > 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Try a stronger password")
            msg.setInformativeText("""
            Password Requirements:
            length=8,  # min length: 8
            uppercase=2,  # need min. 2 uppercase letters
            numbers=2,  # need min. 2 digits
            special=2,  # need min. 2 special characters
            nonletters=2,  # need min. 2 non-letter characters (digits, specials, anything)""")
            msg.setWindowTitle("Bad Password")
            msg.exec()
        else:
            success = database.register(firstname, lastname, address, phonenumber, email, username, password, secretQuestion)
            if success:
                print("Registration Complete")
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Registration Complete")
                msg.setWindowTitle("Continue to Login")
                msg.exec()
                return True
            else:
                print("Registration Failed")
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Please enter a new username")
                msg.setWindowTitle("Username already taken")
                msg.exec()
                return False


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = registrationWindow()
    widget.show()

    app.exec_()