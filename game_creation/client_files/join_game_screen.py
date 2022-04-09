from PyQt5 import QtCore, QtGui, QtWidgets
from client_data import ClientInfo


class JoinGame(object):
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
        self.password_edit = QtWidgets.QLineEdit(Dialog)
        self.password_edit.setMinimumSize(QtCore.QSize(0, 50))
        self.password_edit.setText("")
        self.password_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_edit.setReadOnly(False)
        self.password_edit.setClearButtonEnabled(False)
        self.password_edit.setObjectName("lineEdit_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.password_edit)
        self.verticalLayout.addLayout(self.formLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.join_button = QtWidgets.QPushButton(Dialog)
        self.join_button.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.join_button)
        self.join_button.clicked.connect(self.join_button_pressed)

        self.game_id = ''

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        ClientInfo.join_gui = self

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Join Game"))
        self.label.setText(_translate("Dialog", "Join game"))
        self.label_3.setText(_translate("Dialog", "Password"))
        self.join_button.setText(_translate("Dialog", "Join"))
        self.dialog = Dialog

    def join_button_pressed(self):
        ClientInfo.tcpHandler.join_game(password=self.password_edit.text(), game_id=self.game_id)

    def join_game_success(self):
        ClientInfo.game_owner = False
        ClientInfo.logger.info('Closing join game screen')
        ClientInfo.join_gui = None
        self.dialog.close()
