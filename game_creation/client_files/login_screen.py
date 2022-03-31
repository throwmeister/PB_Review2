from PyQt5 import QtCore, QtGui, QtWidgets
from client_data import ClientInfo

class Login(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Login")
        Dialog.resize(453, 345)
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
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(0, QtWidgets.QFormLayout.LabelRole, spacerItem)
        self.username_label = QtWidgets.QLabel(Dialog)
        self.username_label.setMinimumSize(QtCore.QSize(100, 30))
        self.username_label.setObjectName("username_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.username_label)
        self.username_line = QtWidgets.QLineEdit(Dialog)
        self.username_line.setMinimumSize(QtCore.QSize(100, 50))
        self.username_line.setText("")
        self.username_line.setObjectName("username_line")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.username_line)
        self.password_label = QtWidgets.QLabel(Dialog)
        self.password_label.setObjectName("password_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.password_label)
        self.password_line = QtWidgets.QLineEdit(Dialog)
        self.password_line.setMinimumSize(QtCore.QSize(0, 50))
        self.password_line.setText("")
        self.password_line.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_line.setReadOnly(False)
        self.password_line.setClearButtonEnabled(False)
        self.password_line.setObjectName("password_line")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.password_line)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(3, QtWidgets.QFormLayout.LabelRole, spacerItem1)
        self.verticalLayout.addLayout(self.formLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.login_button = QtWidgets.QPushButton(Dialog)
        self.login_button.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.login_button, 0, QtCore.Qt.AlignBottom)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        self.login_button.clicked.connect(self.login_button_clicked)
        ClientInfo.login_gui = self


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Login", "Login"))
        self.label.setText(_translate("Login", "CLIENT LOGIN"))
        self.username_label.setText(_translate("Login", "Username"))
        self.password_label.setText(_translate("Login", "Password"))
        self.login_button.setText(_translate("Login", "Login"))
        Dialog.close()
        self.dialog = Dialog
        self.dialog.close()

    def login_button_clicked(self):
        ClientInfo.tcpHandler.send_login(self.username_line.text(), self.password_line.text())

    def login_response_success(self):
        ClientInfo.logger.info('Closing login window')
        ClientInfo.login_gui = None
        self.dialog.close()

    def login_response_failed(self):
        pass
