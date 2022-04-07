from PyQt5 import QtCore, QtGui, QtWidgets
from client_data import ClientInfo
import game_creation.shared_directory.data_format as form

class CreateGame(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(509, 378)
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
        self.game_name_label = QtWidgets.QLabel(Dialog)
        self.game_name_label.setMinimumSize(QtCore.QSize(100, 30))
        self.game_name_label.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.game_name_label)
        self.game_name_edit = QtWidgets.QLineEdit(Dialog)
        self.game_name_edit.setMinimumSize(QtCore.QSize(100, 50))
        self.game_name_edit.setText("")
        self.game_name_edit.setObjectName("lineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.game_name_edit)
        self.password_labell = QtWidgets.QLabel(Dialog)
        self.password_labell.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.password_labell)
        self.password_edit = QtWidgets.QLineEdit(Dialog)
        self.password_edit.setMinimumSize(QtCore.QSize(0, 50))
        self.password_edit.setText("")
        self.password_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_edit.setReadOnly(False)
        self.password_edit.setClearButtonEnabled(False)
        self.password_edit.setObjectName("lineEdit_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.password_edit)
        self.type_label = QtWidgets.QLabel(Dialog)
        self.type_label.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.type_label)
        self.type_box = QtWidgets.QComboBox(Dialog)
        self.type_box.setMinimumSize(QtCore.QSize(0, 50))
        self.type_box.setObjectName("comboBox")
        self.type_box.addItem("")
        self.type_box.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.type_box)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(0, QtWidgets.QFormLayout.LabelRole, spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(4, QtWidgets.QFormLayout.LabelRole, spacerItem1)
        self.verticalLayout.addLayout(self.formLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cancel = QtWidgets.QPushButton(Dialog)
        self.cancel.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.cancel, 0, QtCore.Qt.AlignBottom)
        self.create = QtWidgets.QPushButton(Dialog)
        self.create.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.create, 0, QtCore.Qt.AlignBottom)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.create.clicked.connect(self.create_game_button_pressed)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "CREATE GAME"))
        self.game_name_label.setText(_translate("Dialog", "Game name"))
        self.password_labell.setText(_translate("Dialog", "Password"))
        self.type_label.setText(_translate("Dialog", "Game Type"))
        self.type_box.setItemText(0, _translate("Dialog", "Poker"))
        self.type_box.setItemText(1, _translate("Dialog", "Blackjack"))
        self.cancel.setText(_translate("Dialog", "Cancel"))
        self.create.setText(_translate("Dialog", "Create"))
        self.type_box_dict = {'Poker': form.GameTypeEnum.POKER,
                              'Blackjack': form.GameTypeEnum.BLACKJACK}
        self.dialog = Dialog

    def create_game_button_pressed(self):
        game_type = self.type_box_dict[self.type_box.currentData(0)]
        name = self.game_name_edit.text()
        password = self.game_name_edit.text()
        ClientInfo.tcpHandler.create_game(name=name, game_type=game_type, password=password)

    def create_response_success(self):
        ClientInfo.game_owner = True
        ClientInfo.logger.info('Closing create game screen')
        ClientInfo.create_game_gui = None
        self.dialog.close()

    def create_response_failure(self):
        pass
