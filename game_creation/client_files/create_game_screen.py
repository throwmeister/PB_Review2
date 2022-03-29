from PyQt5 import QtCore, QtGui, QtWidgets


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
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setMinimumSize(QtCore.QSize(100, 30))
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setMinimumSize(QtCore.QSize(100, 50))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(0, 50))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setReadOnly(False)
        self.lineEdit_2.setClearButtonEnabled(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 50))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.comboBox)
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

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "CREATE GAME"))
        self.label_2.setText(_translate("Dialog", "Game name"))
        self.label_3.setText(_translate("Dialog", "Password"))
        self.label_4.setText(_translate("Dialog", "TextLabel"))
        self.comboBox.setItemText(0, _translate("Dialog", "Poker"))
        self.comboBox.setItemText(1, _translate("Dialog", "Blackjack"))
        self.cancel.setText(_translate("Dialog", "Cancel"))
        self.create.setText(_translate("Dialog", "Create"))
