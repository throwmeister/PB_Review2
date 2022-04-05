from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1098, 837)
        Form.setStyleSheet("QWidget{\n"
"    background-color: rgb(15, 102, 72);\n"
"    \n"
"}\n"
"\n"
"QLabel{\n"
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
"            }")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.EMPTY = QtWidgets.QLabel(Form)
        self.EMPTY.setAlignment(QtCore.Qt.AlignCenter)
        self.EMPTY.setObjectName("label")
        self.verticalLayout.addWidget(self.EMPTY)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.card2 = QtWidgets.QLabel(Form)
        self.card2.setMinimumSize(QtCore.QSize(200, 100))
        self.card2.setMaximumSize(QtCore.QSize(200, 300))
        self.card2.setText("")
        self.card2.setPixmap(QtGui.QPixmap("C:/Users/alexa/Documents/POKER_BLACKJACK_UIS\\PNG-cards-1.3/2_of_clubs.png"))
        self.card2.setScaledContents(True)
        self.card2.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.card2, 0, QtCore.Qt.AlignVCenter)
        self.card3 = QtWidgets.QLabel(Form)
        self.card3.setMaximumSize(QtCore.QSize(200, 300))
        self.card3.setText("")
        self.card3.setPixmap(QtGui.QPixmap("C:/Users/alexa/Documents/POKER_BLACKJACK_UIS\\PNG-cards-1.3/2_of_diamonds.png"))
        self.card3.setScaledContents(True)
        self.card3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.card3, 0, QtCore.Qt.AlignVCenter)
        self.card4 = QtWidgets.QLabel(Form)
        self.card4.setMaximumSize(QtCore.QSize(200, 300))
        self.card4.setText("")
        self.card4.setPixmap(QtGui.QPixmap("C:/Users/alexa/Documents/POKER_BLACKJACK_UIS\\PNG-cards-1.3/2_of_hearts.png"))
        self.card4.setScaledContents(True)
        self.card4.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.card4, 0, QtCore.Qt.AlignVCenter)
        self.card5 = QtWidgets.QLabel(Form)
        self.card5.setMaximumSize(QtCore.QSize(200, 300))
        self.card5.setText("")
        self.card5.setPixmap(QtGui.QPixmap("C:/Users/alexa/Documents/POKER_BLACKJACK_UIS\\PNG-cards-1.3/3_of_clubs.png"))
        self.card5.setScaledContents(True)
        self.card5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.card5, 0, QtCore.Qt.AlignVCenter)
        self.card6 = QtWidgets.QLabel(Form)
        self.card6.setMaximumSize(QtCore.QSize(200, 300))
        self.card6.setText("")
        self.card6.setPixmap(QtGui.QPixmap("C:/Users/alexa/Documents/POKER_BLACKJACK_UIS\\PNG-cards-1.3/3_of_diamonds.png"))
        self.card6.setScaledContents(True)
        self.card6.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.card6, 0, QtCore.Qt.AlignVCenter)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.EMPTY.setText(_translate("Form", "EMPTY SPACE"))
