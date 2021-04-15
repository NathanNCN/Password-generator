from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QCheckBox,QSlider,QMessageBox
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import random
import sys


class mainwindow(QMainWindow):
    def __init__(self):
        super(mainwindow, self).__init__()
        self.initUI()
        self.password_attributes = []
        self.numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ]
        self.math_symbols = ["*", "%", "(", ")", "/", "+", "=", "-", ">", "<", ]
        self.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                        't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.caps_letters = ['A', 'B', 'C', 'd', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'l', 'M', 'N', 'O', 'P', 'Q', 'R',
                             'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.speical_chacathers = ["!", "`", "~", "@", "#", "$", "&", "_", "}", "{", "\"", "\'", ",", "."]
        self.passwords=[]

    def initUI(self):
        self.setGeometry(350, 200, 600, 400)
        self.setWindowTitle('Password generator')

        # title of the window
        self.title = QtWidgets.QLabel('Times', self)
        self.title.setFont(QFont('Times', 20))
        self.title.setText('Password Generator')
        self.title.move(180, 10)
        self.title.resize(250, 80)

        # atturtuibes of the password

        # length of the password
        self.length_of_password = QtWidgets.QLineEdit(self)
        self.length_of_password.setDisabled(True)
        self.length_of_password.setText('0')
        self.length_of_password.resize(150, 40)
        self.length_of_password.move(40, 115)

        self.add_length = QtWidgets.QPushButton(self)
        self.add_length.setText("A")
        self.add_length.move(170, 115)
        self.add_length.resize(20, 20)
        self.add_length.setObjectName("length_of_password")
        self.add_length.clicked.connect(self.add_or_sub)

        self.remove_length = QtWidgets.QPushButton(self)
        self.remove_length.setText("S")
        self.remove_length.move(170, 135)
        self.remove_length.resize(20, 20)
        self.remove_length.setObjectName("length_of_password")
        self.remove_length.clicked.connect(self.add_or_sub)

        self.len_of_pass = QtWidgets.QLabel(self)
        self.len_of_pass.setText('Length of password')
        self.len_of_pass.setFont(QFont('Times', 10))
        self.len_of_pass.move(40, 80)
        self.len_of_pass.resize(250, 40)

        # password add special characters

        self.add_special = QtWidgets.QLabel(self)
        self.add_special.setText('Add special characters. (^ < > , . \' \" ` ~)')
        self.add_special.setFont(QFont('Times', 10))
        self.add_special.move(40, 150)
        self.add_special.resize(250, 40)

        self.checkbox1 = QCheckBox(self)
        self.checkbox1.move(300, 165)

        # password adds capital letters
        self.add_caps = QtWidgets.QLabel(self)
        self.add_caps.setText('Add capital letters. (A B C D)')
        self.add_caps.setFont(QFont('Times', 10))
        self.add_caps.move(40, 180)
        self.add_caps.resize(250, 40)

        self.checkbox2 = QCheckBox(self)
        self.checkbox2.move(300, 192)

        # password add letters
        self.add_letters = QtWidgets.QLabel(self)
        self.add_letters.setText('Add letters. (a b c d)')
        self.add_letters.setFont(QFont('Times', 10))
        self.add_letters.move(40, 210)
        self.add_letters.resize(250, 40)

        self.checkbox3 = QCheckBox(self)
        self.checkbox3.move(300, 219)

        self.add_numbers = QtWidgets.QLabel(self)
        self.add_numbers.setText('Add numbers. (1 2 3 4)')
        self.add_numbers.setFont(QFont('Times', 10))
        self.add_numbers.move(40, 240)
        self.add_numbers.resize(250, 40)

        self.checkbox4 = QCheckBox(self)
        self.checkbox4.move(300, 246)

        # password add math symbols
        self.add_math_symbols = QtWidgets.QLabel(self)
        self.add_math_symbols.setText('Add math symbols. (+ - = /)')
        self.add_math_symbols.setFont(QFont('Times', 10))
        self.add_math_symbols.move(40, 270)
        self.add_math_symbols.resize(250, 40)

        self.checkbox5 = QCheckBox(self)
        self.checkbox5.move(300, 280)

        # amount of passwords
        self.amount_of_passwords = QtWidgets.QLineEdit(self)
        self.amount_of_passwords.setDisabled(True)
        self.amount_of_passwords.setText('0')
        self.amount_of_passwords.resize(150, 40)
        self.amount_of_passwords.move(375, 115)

        self.add_passwords = QtWidgets.QPushButton(self)
        self.add_passwords.setText("A")
        self.add_passwords.move(505, 115)
        self.add_passwords.resize(20, 20)
        self.add_passwords.clicked.connect(self.add_or_sub)

        self.remove_passwords = QtWidgets.QPushButton(self)
        self.remove_passwords.setText("S")
        self.remove_passwords.move(505, 135)
        self.remove_passwords.resize(20, 20)
        self.remove_passwords.clicked.connect(self.add_or_sub)

        self.amount_of_pass = QtWidgets.QLabel(self)
        self.amount_of_pass.setText('Add amount of passwords')
        self.amount_of_pass.setFont(QFont('Times', 10))
        self.amount_of_pass.move(375, 80)
        self.amount_of_pass.resize(250, 40)

        # submit password with attrubites
        self.submit_password = QtWidgets.QPushButton(self)
        self.submit_password.setText("Get Passwords")
        self.submit_password.move(375, 165)
        self.submit_password.resize(150, 40)
        self.submit_password.clicked.connect(self.submit)

        #slide down for information
        self.slider = QSlider(Qt.Vertical, self)
        self.slider.valueChanged.connect(self.updateLabel)
        self.slider.resize(30,75)
        self.slider.move(515,250)
        self.slider.setInvertedAppearance(True)
        self.slider.setDisabled(True)

        #display passwords
        self.display_passwords = QtWidgets.QLabel(self)
        self.display_passwords.setFont(QFont('Times', 10))
        self.display_passwords.setText('')
        self.display_passwords.move(375, 230)




    def add_or_sub(self):
        sender = self.sender()
        if sender.objectName() == "length_of_password":
            if sender.text() == self.remove_passwords.text():
                if int(self.length_of_password.text()) != 0:
                    self.length_of_password.setText(str(int(self.length_of_password.text()) - 1))
            else:
                self.length_of_password.setText(str(int(self.length_of_password.text()) + 1))
        else:
            if sender.text() == self.remove_passwords.text():
                if int(self.amount_of_passwords.text()) != 0:
                    self.amount_of_passwords.setText(str(int(self.amount_of_passwords.text()) - 1))
            else:
                self.amount_of_passwords.setText(str(int(self.amount_of_passwords.text()) + 1))

    def submit(self):
        if int(self.length_of_password.text()) != 0 and int(self.amount_of_passwords.text()) !=0:
            minmal_len = 0
            amount_of_passwords = int(self.amount_of_passwords.text())
            lenght_of_password = int(self.length_of_password.text())
            if self.checkbox1.isChecked() == True:
                self.password_attributes.append(self.speical_chacathers)
                minmal_len+=1
            if self.checkbox2.isChecked() == True:
                self.password_attributes.append(self.caps_letters)
                minmal_len+=1

            if self.checkbox3.isChecked() == True:
                self.password_attributes.append(self.letters)
                minmal_len+=1

            if self.checkbox4.isChecked() == True:
                self.password_attributes.append(self.numbers)
                minmal_len+=1

            if self.checkbox5.isChecked() == True:
                self.password_attributes.append(self.math_symbols)
                minmal_len+=1

            if int(self.length_of_password.text())<minmal_len:
                QMessageBox.about(self, "Problem","Your password is not long enough for the attributes that you want")
                self.password_attributes=[]
            if minmal_len==0:
                QMessageBox.about(self, "Problem","Make sure you have atleast one attribute")
            else:
                for passwords in range(0, amount_of_passwords):
                    password = ''
                    must_have = [x for x in range(0, minmal_len)]
                    random.shuffle(must_have)
                    for letters in range(0,lenght_of_password):
                        if len(must_have)!=0:
                            password+=random.choice(self.password_attributes[must_have[0]])
                            must_have.pop(0)
                        else:
                            password+=random.choice(random.choice(self.password_attributes))
                    password=list(password)
                    random.shuffle(password)
                    self.passwords.append("".join(password))
                print(self.passwords)
                self.slider.setDisabled(False)
                self.slider.setRange(0,len(self.passwords))
                self.display_passwords.setText('\n'.join(self.passwords[0:5]))
                self.display_passwords.adjustSize()
                if len(self.passwords)<=5:
                    self.slider.hide()
                else:
                    self.slider.setRange(5, len(self.passwords))
        else:
            QMessageBox.about(self, "Problem", "Make sure you have a password that is atleast 1 character and atleast 1 password")

    def updateLabel(self, value):
        value=self.slider.value()
        self.display_passwords.setText('\n'.join(self.passwords[value-5:value]))



def main():
    app = QApplication(sys.argv)
    win = mainwindow()
    win.show()
    app.exec_()


main()
