from PyQt5 import QtCore, QtGui, QtWidgets
from client_data import ClientInfo, GameInfo


class Bet(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setMinimumSize(QtCore.QSize(480, 307))
        Dialog.setMaximumSize(QtCore.QSize(480, 370))
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
                                 "                ")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.bet_edit = QtWidgets.QLineEdit(Dialog)
        self.bet_edit.setMinimumSize(QtCore.QSize(0, 50))
        self.bet_edit.setText("")
        self.bet_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.bet_edit.setClearButtonEnabled(False)
        self.bet_edit.setObjectName("lineEdit_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.bet_edit)
        self.verticalLayout.addLayout(self.formLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.bet_button = QtWidgets.QPushButton(Dialog)
        self.bet_button.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.bet_button)
        self.bet_button.clicked.connect(self.bet_button_pressed)
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        ClientInfo.bet_gui = self

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Bet"))
        self.label.setText(_translate("Dialog", "How much would you like to bet"))
        self.label_3.setText(_translate("Dialog", "Amount"))
        self.bet_button.setText(_translate("Dialog", "Bet"))
        self.dialog = Dialog

    def bet_button_pressed(self):
        self.bet_button.setDisabled(True)
        try:
            amount = int(self.bet_edit.text())
            if 0 <= amount < GameInfo.bet:
                ClientInfo.logger.info('Sending bet amount')
                ClientInfo.tcpHandler.send_bet(amount)
            else:
                self.bet_button.setDisabled(False)
                ClientInfo.logger.error('Invalid amount')
        except ValueError:
            self.bet_button.setDisabled(False)
            ClientInfo.logger.error('Invalid character')

    def bet_success(self):
        ClientInfo.bet_gui = None
        self.dialog.close()

    def bet_error(self):
        ClientInfo.logger.info('Bet error')
        self.bet_button.setDisabled(False)
