

from PyQt5 import QtCore, QtGui, QtWidgets


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
        self.bank_red_chip.setPixmap(QtGui.QPixmap("C:/Users/alexa/Documents/POKER_BLACKJACK_UIS\\../../Downloads/PngItem_1441202.png"))
        self.bank_red_chip.setScaledContents(True)
        self.bank_red_chip.setObjectName("bank_red_chip")
        self.horizontalLayout_2.addWidget(self.bank_red_chip)
        self.bank_blue_chip = QtWidgets.QLabel(Dialog)
        self.bank_blue_chip.setMaximumSize(QtCore.QSize(100, 100))
        self.bank_blue_chip.setText("")
        self.bank_blue_chip.setPixmap(QtGui.QPixmap("C:/Users/alexa/Documents/POKER_BLACKJACK_UIS\\../../Downloads/PngItem_292913.png"))
        self.bank_blue_chip.setScaledContents(True)
        self.bank_blue_chip.setObjectName("bank_blue_chip")
        self.horizontalLayout_2.addWidget(self.bank_blue_chip)
        self.bank_brown_chip = QtWidgets.QLabel(Dialog)
        self.bank_brown_chip.setMaximumSize(QtCore.QSize(100, 100))
        self.bank_brown_chip.setText("")
        self.bank_brown_chip.setPixmap(QtGui.QPixmap("C:/Users/alexa/Documents/POKER_BLACKJACK_UIS\\../../Downloads/brown_chip.png"))
        self.bank_brown_chip.setScaledContents(True)
        self.bank_brown_chip.setObjectName("bank_brown_chip")
        self.horizontalLayout_2.addWidget(self.bank_brown_chip)
        self.bank_black_chip = QtWidgets.QLabel(Dialog)
        self.bank_black_chip.setMaximumSize(QtCore.QSize(100, 100))
        self.bank_black_chip.setText("")
        self.bank_black_chip.setPixmap(QtGui.QPixmap("C:/Users/alexa/Documents/POKER_BLACKJACK_UIS\\../../Downloads/black_chip.png"))
        self.bank_black_chip.setScaledContents(True)
        self.bank_black_chip.setObjectName("bank_black_chip")
        self.horizontalLayout_2.addWidget(self.bank_black_chip)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setMaximumSize(QtCore.QSize(400, 50))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(-1)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("font-family: MS Shell Dlg 2;\n"
"    font-size: 30px;\n"
"color: rgb(170, 85, 255);\n"
"                \n"
"                ")
        self.label_10.setObjectName("label_10")
        self.verticalLayout_3.addWidget(self.label_10, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setMaximumSize(QtCore.QSize(100, 100))
        self.label_11.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_4.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setMaximumSize(QtCore.QSize(100, 100))
        self.label_12.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_4.addWidget(self.label_12)
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setMaximumSize(QtCore.QSize(100, 100))
        self.label_13.setScaledContents(False)
        self.label_13.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_13.setWordWrap(False)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_4.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setMaximumSize(QtCore.QSize(100, 100))
        self.label_14.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_4.addWidget(self.label_14)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.bet_red_chip = QtWidgets.QLabel(Dialog)
        self.bet_red_chip.setMinimumSize(QtCore.QSize(100, 100))
        self.bet_red_chip.setMaximumSize(QtCore.QSize(100, 100))
        self.bet_red_chip.setText("")
        self.bet_red_chip.setPixmap(QtGui.QPixmap("C:/Users/alexa/Documents/POKER_BLACKJACK_UIS\\../../Downloads/PngItem_1441202.png"))
        self.bet_red_chip.setScaledContents(True)
        self.bet_red_chip.setObjectName("bet_red_chip")
        self.horizontalLayout_5.addWidget(self.bet_red_chip)
        self.bet_blue_chip = QtWidgets.QLabel(Dialog)
        self.bet_blue_chip.setMaximumSize(QtCore.QSize(100, 100))
        self.bet_blue_chip.setText("")
        self.bet_blue_chip.setPixmap(QtGui.QPixmap("C:/Users/alexa/Documents/POKER_BLACKJACK_UIS\\../../Downloads/PngItem_292913.png"))
        self.bet_blue_chip.setScaledContents(True)
        self.bet_blue_chip.setObjectName("bet_blue_chip")
        self.horizontalLayout_5.addWidget(self.bet_blue_chip)
        self.bet_brown_chip = QtWidgets.QLabel(Dialog)
        self.bet_brown_chip.setMaximumSize(QtCore.QSize(100, 100))
        self.bet_brown_chip.setText("")
        self.bet_brown_chip.setPixmap(QtGui.QPixmap("C:/Users/alexa/Documents/POKER_BLACKJACK_UIS\\../../Downloads/brown_chip.png"))
        self.bet_brown_chip.setScaledContents(True)
        self.bet_brown_chip.setObjectName("bet_brown_chip")
        self.horizontalLayout_5.addWidget(self.bet_brown_chip)
        self.bet_black_chip = QtWidgets.QLabel(Dialog)
        self.bet_black_chip.setMaximumSize(QtCore.QSize(100, 100))
        self.bet_black_chip.setText("")
        self.bet_black_chip.setPixmap(QtGui.QPixmap("C:/Users/alexa/Documents/POKER_BLACKJACK_UIS\\../../Downloads/black_chip.png"))
        self.bet_black_chip.setScaledContents(True)
        self.bet_black_chip.setObjectName("bet_black_chip")
        self.horizontalLayout_5.addWidget(self.bet_black_chip)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.bet_list = QtWidgets.QListWidget(Dialog)
        self.bet_list.setObjectName("bet_list")
        self.verticalLayout_2.addWidget(self.bet_list)
        self.bet_fold_button = QtWidgets.QPushButton(Dialog)
        self.bet_fold_button.setObjectName("bet_fold_button")
        self.verticalLayout_2.addWidget(self.bet_fold_button)
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
        self.label.setText(_translate("Dialog", "Balance: 75"))
        self.label_7.setText(_translate("Dialog", "5"))
        self.label_6.setText(_translate("Dialog", "5"))
        self.label_8.setText(_translate("Dialog", "5"))
        self.label_9.setText(_translate("Dialog", "5"))
        self.label_10.setText(_translate("Dialog", "Betting: 0"))
        self.label_11.setText(_translate("Dialog", "0"))
        self.label_12.setText(_translate("Dialog", "0"))
        self.label_13.setText(_translate("Dialog", "0"))
        self.label_14.setText(_translate("Dialog", "0"))
        self.bet_fold_button.setText(_translate("Dialog", "Fold"))
        self.bet_button.setText(_translate("Dialog", "Bet"))
