

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
        self.bet_stack = QtWidgets.QWidget()
        self.red_chip_icon = "images/chips/red_chip.png"
        self.blue_chip_icon = "images/chips/blue_chip.png"
        self.brown_chip_icon = "images/chips/brown_chip.png"
        self.black_chip_icon = "images/chips/black_chip"
        self.bet_vert_layout = QtWidgets.QVBoxLayout(self.bet_stack)
        self.bet_vert_layout.setObjectName("verticalLayout_2")
        self.bet_vert_layout2 = QtWidgets.QVBoxLayout()
        self.bet_vert_layout2.setObjectName("verticalLayout")
        self.bank_balance = QtWidgets.QLabel(self.bet_stack)
        self.bank_balance.setMaximumSize(QtCore.QSize(400, 50))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(-1)
        self.bank_balance.setFont(font)
        self.bank_balance.setStyleSheet("font-family: MS Shell Dlg 2;\n"
"    font-size: 30px;\n"
"")
        self.bank_balance.setObjectName("label")
        self.bet_vert_layout2.addWidget(self.bank_balance, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.bank_counter_red = QtWidgets.QLabel(self.bet_stack)
        self.bank_counter_red.setMaximumSize(QtCore.QSize(100, 100))
        self.bank_counter_red.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.bank_counter_red.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.bank_counter_red)
        self.bank_counter_blue = QtWidgets.QLabel(self.bet_stack)
        self.bank_counter_blue.setMaximumSize(QtCore.QSize(100, 100))
        self.bank_counter_blue.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.bank_counter_blue.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.bank_counter_blue)
        self.bank_counter_brown = QtWidgets.QLabel(self.bet_stacl)
        self.bank_counter_brown.setMaximumSize(QtCore.QSize(100, 100))
        self.bank_counter_brown.setScaledContents(False)
        self.bank_counter_brown.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.bank_counter_brown.setWordWrap(False)
        self.bank_counter_brown.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.bank_counter_brown)
        self.bank_counter_black = QtWidgets.QLabel(self.bet_stack)
        self.bank_counter_black.setMaximumSize(QtCore.QSize(100, 100))
        self.bank_counter_black.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.bank_counter_black.setObjectName("label_9")
        self.horizontalLayout_3.addWidget(self.bank_counter_black)
        self.bet_vert_layout2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.bank_red_chip = BankChip(self.bet_stack, self.bank_chip_clicked)
        self.bank_red_chip.setMinimumSize(QtCore.QSize(100, 100))
        self.bank_red_chip.setMaximumSize(QtCore.QSize(100, 100))
        self.bank_red_chip.setText("")
        self.bank_red_chip.setPixmap(QtGui.QPixmap(self.red_chip_icon))
        self.bank_red_chip.setScaledContents(True)
        self.bank_red_chip.setObjectName("bank_red_chip")
        self.horizontalLayout_2.addWidget(self.bank_red_chip)
        self.bank_blue_chip = BankChip(self.bet_stack, self.bank_chip_clicked)
        self.bank_blue_chip.setMaximumSize(QtCore.QSize(100, 100))
        self.bank_blue_chip.setText("")
        self.bank_blue_chip.setPixmap(QtGui.QPixmap(self.blue_chip_icon))
        self.bank_blue_chip.setScaledContents(True)
        self.bank_blue_chip.setObjectName("bank_blue_chip")
        self.horizontalLayout_2.addWidget(self.bank_blue_chip)
        self.bank_brown_chip = BankChip(self.bet_stack, self.bank_chip_clicked)
        self.bank_brown_chip.setMaximumSize(QtCore.QSize(100, 100))
        self.bank_brown_chip.setText("")
        self.bank_brown_chip.setPixmap(QtGui.QPixmap(self.brown_chip_icon))
        self.bank_brown_chip.setScaledContents(True)
        self.bank_brown_chip.setObjectName("bank_brown_chip")
        self.horizontalLayout_2.addWidget(self.bank_brown_chip)
        self.bank_black_chip = BankChip(self.bet_stack, self.bank_chip_clicked)
        self.bank_black_chip.setMaximumSize(QtCore.QSize(100, 100))
        self.bank_black_chip.setText("")
        self.bank_black_chip.setPixmap(QtGui.QPixmap(self.black_chip_icon))
        self.bank_black_chip.setScaledContents(True)
        self.bank_black_chip.setObjectName("bank_black_chip")
        self.horizontalLayout_2.addWidget(self.bank_black_chip)
        self.bet_vert_layout2.addLayout(self.horizontalLayout_2)
        self.bet_vert_layout.addLayout(self.bet_vert_layout2)
        self.bet_hz_layout3 = QtWidgets.QVBoxLayout()
        self.bet_hz_layout3.setObjectName("verticalLayout_3")
        self.bet_balance = QtWidgets.QLabel(self.bet_stack)
        self.bet_balance.setMaximumSize(QtCore.QSize(400, 50))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(-1)
        self.bet_balance.setFont(font)
        self.bet_balance.setStyleSheet("font-family: MS Shell Dlg 2;\n"
"    font-size: 30px;\n"
"color: rgb(170, 85, 255);\n"
"                \n"
"                ")
        self.bet_balance.setObjectName("label_10")
        self.bet_hz_layout3.addWidget(self.bet_balance, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.bet_counter_red = QtWidgets.QLabel(self.bet_stack)
        self.bet_counter_red.setMaximumSize(QtCore.QSize(100, 100))
        self.bet_counter_red.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.bet_counter_red.setObjectName("label_11")
        self.horizontalLayout_4.addWidget(self.bet_counter_red)
        self.bet_counter_blue = QtWidgets.QLabel(self.bet_stack)
        self.bet_counter_blue.setMaximumSize(QtCore.QSize(100, 100))
        self.bet_counter_blue.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.bet_counter_blue.setObjectName("label_12")
        self.horizontalLayout_4.addWidget(self.bet_counter_blue)
        self.bet_counter_brown = QtWidgets.QLabel(self.bet_stack)
        self.bet_counter_brown.setMaximumSize(QtCore.QSize(100, 100))
        self.bet_counter_brown.setScaledContents(False)
        self.bet_counter_brown.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.bet_counter_brown.setWordWrap(False)
        self.bet_counter_brown.setObjectName("label_13")
        self.horizontalLayout_4.addWidget(self.bet_counter_brown)
        self.bet_counter_black = QtWidgets.QLabel(self.bet_stack)
        self.bet_counter_black.setMaximumSize(QtCore.QSize(100, 100))
        self.bet_counter_black.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.bet_counter_black.setObjectName("label_14")
        self.horizontalLayout_4.addWidget(self.bet_counter_black)
        self.bet_hz_layout3.addLayout(self.horizontalLayout_4)
        self.bet_hz_bet_layout = QtWidgets.QHBoxLayout()
        self.bet_hz_bet_layout.setObjectName("horizontalLayout_5")
        self.bet_red_chip = BetChip(self.bet_stack, self.bet_chip_clicked)
        self.bet_red_chip.setMinimumSize(QtCore.QSize(100, 100))
        self.bet_red_chip.setMaximumSize(QtCore.QSize(100, 100))
        self.bet_red_chip.setText("")
        self.bet_red_chip.setPixmap(QtGui.QPixmap(self.red_chip_icon))
        self.bet_red_chip.setScaledContents(True)
        self.bet_red_chip.setObjectName("bet_red_chip")
        self.bet_hz_bet_layout.addWidget(self.bet_red_chip)
        self.bet_blue_chip = BetChip(self.bet_stack, self.bet_chip_clicked)
        self.bet_blue_chip.setMaximumSize(QtCore.QSize(100, 100))
        self.bet_blue_chip.setText("")
        self.bet_blue_chip.setPixmap(QtGui.QPixmap(self.blue_chip_icon))
        self.bet_blue_chip.setScaledContents(True)
        self.bet_blue_chip.setObjectName("bet_blue_chip")
        self.bet_hz_bet_layout.addWidget(self.bet_blue_chip)
        self.bet_brown_chip = BetChip(self.bet_stack, self.bet_chip_clicked)
        self.bet_brown_chip.setMaximumSize(QtCore.QSize(100, 100))
        self.bet_brown_chip.setText("")
        self.bet_brown_chip.setPixmap(QtGui.QPixmap(self.brown_chip_icon))
        self.bet_brown_chip.setScaledContents(True)
        self.bet_brown_chip.setObjectName("bet_brown_chip")
        self.bet_hz_bet_layout.addWidget(self.bet_brown_chip)
        self.bet_black_chip = BetChip(self.bet_stack, self.bet_chip_clicked)
        self.bet_black_chip.setMaximumSize(QtCore.QSize(100, 100))
        self.bet_black_chip.setText("")
        self.bet_black_chip.setPixmap(QtGui.QPixmap(self.black_chip_icon))
        self.bet_black_chip.setScaledContents(True)
        self.bet_black_chip.setObjectName("bet_black_chip")
        self.bet_hz_bet_layout.addWidget(self.bet_black_chip)
        self.bet_hz_layout3.addLayout(self.bet_hz_bet_layout)
        self.bet_vert_layout.addLayout(self.bet_hz_layout3)
        self.bet_list = QtWidgets.QListWidget(self.bet_stack)
        self.bet_list.setObjectName("bet_list")
        self.bet_vert_layout.addWidget(self.bet_list)
        self.bet_fold_button = QtWidgets.QPushButton(self.bet_stack)
        self.bet_fold_button.setObjectName("bet_fold_button")
        self.bet_vert_layout.addWidget(self.bet_fold_button)
        self.bet_hz_layout = QtWidgets.QHBoxLayout()
        self.bet_hz_layout.setObjectName("horizontalLayout")
        self.bet_button = QtWidgets.QPushButton(self.bet_stack)
        self.bet_button.setObjectName("bet_button")
        self.bet_hz_layout.addWidget(self.bet_button, 0, QtCore.Qt.AlignBottom)
        self.bet_vert_layout.addLayout(self.bet_hz_layout)

        self.bank_red_chip.set_value(1)
        self.bet_red_chip.set_value(1)
        self.bank_blue_chip.set_value(2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def setup_bet_screen(self):
        pass


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.bank_balance.setText(_translate("Dialog", "Balance: 75"))
        self.bank_counter_red.setText(_translate("Dialog", "b_r"))
        self.bank_counter_blue.setText(_translate("Dialog", "b_blu"))
        self.bank_counter_brown.setText(_translate("Dialog", "b_br"))
        self.bank_counter_black.setText(_translate("Dialog", "b_bla"))
        self.bet_balance.setText(_translate("Dialog", "Betting: 0"))
        self.bet_counter_red.setText(_translate("Dialog", "b_r"))
        self.bet_counter_blue.setText(_translate("Dialog", "b_blu"))
        self.bet_counter_brown.setText(_translate("Dialog", "b_br"))
        self.bet_counter_black.setText(_translate("Dialog", "b_bla"))
        self.bet_fold_button.setText(_translate("Dialog", "Fold"))
        self.bet_button.setText(_translate("Dialog", "Bet"))

    def bank_chip_clicked(self, event, chip_obj):
        button = event.button()
        modifiers = event.modifiers()
        if modifiers == QtCore.Qt.NoModifier and button == QtCore.Qt.LeftButton:
            pass

    def bet_chip_clicked(self, event, chip_obj):
        button = event.button()
        modifiers = event.modifiers()
        if modifiers == QtCore.Qt.NoModifier and button == QtCore.Qt.LeftButton:
            pass


class BankChip(QtWidgets.QLabel):
    def __init__(self, form, clicked_func):
        super(BankChip, self).__init__(form)
        self.value = 0
        self.amount = 5
        self.when_clicked = clicked_func

    def set_value(self, val):
        self.value = val

    def mouseReleaseEvent(self, ev):
        self.when_clicked(ev, self)


class BetChip(QtWidgets.QLabel):
    def __init__(self, form, clicked_func):
        super(BetChip, self).__init__(form)
        self.value = 0
        self.amount = 5
        self.when_clicked = clicked_func

    def set_value(self, val):
        self.value = val

    def mouseReleaseEvent(self, ev):
        self.when_clicked(ev, self)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)

    main = QtWidgets.QWidget()
    ui = Ui_Dialog()
    ui.setupUi(main)
    main.show()

    sys.exit(app.exec_())