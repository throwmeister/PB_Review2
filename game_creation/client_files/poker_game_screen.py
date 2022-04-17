from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from bet_screen import Bet
from client_data import ClientInfo, GameInfo
from game_creation.shared_directory import data_format as form


class Game(object):
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
        self.card1 = ExtendedCard(Form)
        self.card1.setMinimumSize(QtCore.QSize(200, 100))
        self.card1.setMaximumSize(QtCore.QSize(200, 300))
        self.card1.setText("")
        self.back_card = "images/back_card.png"
        self.card1.setPixmap(QtGui.QPixmap(self.back_card))
        self.card1.setScaledContents(True)
        self.card1.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.card1, 0, QtCore.Qt.AlignVCenter)
        self.card2 = ExtendedCard(Form)
        self.card2.setMaximumSize(QtCore.QSize(200, 300))
        self.card2.setText("")
        self.card2.setPixmap(QtGui.QPixmap(self.back_card))
        self.card2.setScaledContents(True)
        self.card2.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.card2, 0, QtCore.Qt.AlignVCenter)
        self.card3 = ExtendedCard(Form)
        self.card3.setMaximumSize(QtCore.QSize(200, 300))
        self.card3.setText("")
        self.card3.setPixmap(QtGui.QPixmap(self.back_card))
        self.card3.setScaledContents(True)
        self.card3.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.card3, 0, QtCore.Qt.AlignVCenter)
        self.card4 = ExtendedCard(Form)
        self.card4.setMaximumSize(QtCore.QSize(200, 300))
        self.card4.setText("")
        self.card4.setPixmap(QtGui.QPixmap(self.back_card))
        self.card4.setScaledContents(True)
        self.card4.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.card4, 0, QtCore.Qt.AlignVCenter)
        self.card5 = ExtendedCard(Form)
        self.card5.setMaximumSize(QtCore.QSize(200, 300))
        self.card5.setText("")
        self.card5.setPixmap(QtGui.QPixmap(self.back_card))
        self.card5.setScaledContents(True)
        self.card5.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.card5, 0, QtCore.Qt.AlignVCenter)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        ClientInfo.game_gui = self

        self.card_list = [self.card1, self.card2, self.card3, self.card4, self.card5]
        self.state = form.GameState.BETTING

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setWindowModality(QtCore.Qt.ApplicationModal)
        self.open_bet_screen()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.EMPTY.setText(_translate("Form", "EMPTY SPACE"))

    def open_bet_screen(self):
        self.lwindow = QtWidgets.QDialog()
        self.lui = Bet()
        self.lui.setupUi(self.lwindow)
        self.lwindow.show()
        GameInfo.state = form.GameState.CARD_CHANGING

    def set_cards(self, cards):
        for i, card in enumerate(cards):
            c = form.ExtractCard(card)
            self.card_list[i].set_values(c.suit, c.value)


class ExtendedCard(QtWidgets.QLabel):
    def __init__(self, form):
        super(ExtendedCard, self).__init__(form)
        self.suit = ''
        self.value = 0

    def set_values(self, suit, value):
        self.suit = suit
        self.value = value
        self.setPixmap(QtGui.QPixmap(f'images/PNG-cards-1.3/{value}_of_{suit.lower()}.png'))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = QtWidgets.QWidget()
    ui = Game()
    ui.setupUi(main)
    main.show()
    sys.exit(app.exec_())
