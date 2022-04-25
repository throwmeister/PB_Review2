from PyQt5 import QtCore, QtGui, QtWidgets
from client_data import ClientInfo, GameInfo

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1015, 849)
        Dialog.setStyleSheet("QWidget{\n"
"    background-color: rgb(15, 102, 72);\n"
"    \n"
"}\n"
"\n"
"QLabel{\n"
"font-family: MS Shell Dlg 2;\n"
"    font-size: 22px;\n"
"\n"
"}\n"
"\n"
"QLineEdit{\n"
"font-family: MS Shell Dlg 2;\n"
"    font-size: 18px;\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"    font-family: MS Shell Dlg 2;\n"
"    font-size: 30px;\n"
"                \n"
"    color: rgb(0, 85, 0);\n"
"                \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 132, 93, 255), stop:1 rgba(97, 192, 164, 255));\n"
"                border-radius: 3px;\n"
"                border: 2px groove rgb(0, 0, 0)\n"
"            }\n"
"            QPushButton:hover{\n"
"            background-color: #e3c086;\n"
"            outline: none\n"
"            }\n"
"")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setMaximumSize(QtCore.QSize(400, 50))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(-1)
        self.label.setFont(font)
        self.label.setStyleSheet("font-family: MS Shell Dlg 2;\n"
"    font-size: 30px;\n"
"")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setMaximumSize(QtCore.QSize(100, 100))
        self.label_7.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setMaximumSize(QtCore.QSize(100, 100))
        self.label_6.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setMaximumSize(QtCore.QSize(100, 100))
        self.label_8.setScaledContents(False)
        self.label_8.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_8.setWordWrap(False)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setMaximumSize(QtCore.QSize(100, 100))
        self.label_9.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_3.addWidget(self.label_9)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.bank_red_chip = QtWidgets.QLabel(Dialog)
        self.bank_red_chip.setMinimumSize(QtCore.QSize(100, 100))
        self.bank_red_chip.setMaximumSize(QtCore.QSize(100, 100))
        self.bank_red_chip.setText("")
        self.red_chip_icon = "images/chips/red_chip.png"
        self.blue_chip_icon = "images/chips/blue_chip.png"
        self.brown_chip_icon = "images/chips/brown_chip.png"
        self.black_chip_icon = "images/chips/black_chip.png"
        self.right_arrow_icon = "images/arrow_right.png"
        self.left_arrow_icon = "images/arrow_left.png"
        self.bank_red_chip.setPixmap(QtGui.QPixmap(self.red_chip_icon))
        self.bank_red_chip.setScaledContents(True)
        self.bank_red_chip.setObjectName("bank_red_chip")
        self.horizontalLayout_2.addWidget(self.bank_red_chip)
        self.bank_blue_chip = QtWidgets.QLabel(Dialog)
        self.bank_blue_chip.setMaximumSize(QtCore.QSize(100, 100))
        self.bank_blue_chip.setText("")
        self.bank_blue_chip.setPixmap(QtGui.QPixmap(self.blue_chip_icon))
        self.bank_blue_chip.setScaledContents(True)
        self.bank_blue_chip.setObjectName("bank_blue_chip")
        self.horizontalLayout_2.addWidget(self.bank_blue_chip)
        self.bank_brown_chip = QtWidgets.QLabel(Dialog)
        self.bank_brown_chip.setMaximumSize(QtCore.QSize(100, 100))
        self.bank_brown_chip.setText("")
        self.bank_brown_chip.setPixmap(QtGui.QPixmap(self.brown_chip_icon))
        self.bank_brown_chip.setScaledContents(True)
        self.bank_brown_chip.setObjectName("bank_brown_chip")
        self.horizontalLayout_2.addWidget(self.bank_brown_chip)
        self.bank_black_chip = QtWidgets.QLabel(Dialog)
        self.bank_black_chip.setMaximumSize(QtCore.QSize(100, 100))
        self.bank_black_chip.setText("")
        self.bank_black_chip.setPixmap(QtGui.QPixmap(self.black_chip_icon))
        self.bank_black_chip.setScaledContents(True)
        self.bank_black_chip.setObjectName("bank_black_chip")
        self.horizontalLayout_2.addWidget(self.bank_black_chip)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setMaximumSize(QtCore.QSize(100, 100))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap(self.right_arrow_icon))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_3.addWidget(self.label_10, 0, QtCore.Qt.AlignRight)
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setMaximumSize(QtCore.QSize(100, 100))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("C:/Users/alexa/Documents/POKER_BLACKJACK_UIS\\arrow_left.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_3.addWidget(self.label_11, 0, QtCore.Qt.AlignRight)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setMaximumSize(QtCore.QSize(100, 100))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(self.right_arrow_icon))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter)
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setMaximumSize(QtCore.QSize(100, 100))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("C:/Users/alexa/Documents/POKER_BLACKJACK_UIS\\arrow_left.png"))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_4.addWidget(self.label_12, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setMaximumSize(QtCore.QSize(100, 100))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(self.right_arrow_icon))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2, 0, QtCore.Qt.AlignLeft)
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setMaximumSize(QtCore.QSize(100, 100))
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap(self.right_arrow_icon))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_5.addWidget(self.label_13, 0, QtCore.Qt.AlignLeft)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bet_button = QtWidgets.QPushButton(Dialog)
        self.bet_button.setObjectName("bet_button")
        self.horizontalLayout.addWidget(self.bet_button, 0, QtCore.Qt.AlignBottom)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):

        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Convert"))
        self.label_7.setText(_translate("Dialog", "5"))
        self.label_6.setText(_translate("Dialog", "5"))
        self.label_8.setText(_translate("Dialog", "5"))
        self.label_9.setText(_translate("Dialog", "5"))
        self.bet_button.setText(_translate("Dialog", "Balance: XD"))
