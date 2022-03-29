from PyQt5 import QtCore, QtGui, QtWidgets
from create_game_screen import CreateGame
from login_screen import Login




class Menu(object):
    def setupUi(self, Form):
        Form.setObjectName("Poker and Blackjack")
        Form.resize(1054, 860)
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
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.title = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.verticalLayout.addWidget(self.title)
        self.main_stack = QtWidgets.QStackedWidget(Form)
        self.main_stack.setObjectName("main_stack")
        self.main_menu = QtWidgets.QWidget()
        self.main_menu.setObjectName("main_menu")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.main_menu)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.play_button = QtWidgets.QPushButton(self.main_menu)
        self.play_button.setMinimumSize(QtCore.QSize(450, 100))
        self.play_button.setMaximumSize(QtCore.QSize(450, 100))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(-1)
        self.play_button.setFont(font)
        self.play_button.setObjectName("play_button")
        self.verticalLayout_2.addWidget(self.play_button, 0, QtCore.Qt.AlignHCenter)
        self.settings_button = QtWidgets.QPushButton(self.main_menu)
        self.settings_button.setMinimumSize(QtCore.QSize(450, 100))
        self.settings_button.setMaximumSize(QtCore.QSize(450, 100))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(-1)
        self.settings_button.setFont(font)
        self.settings_button.setObjectName("settings_button")
        self.verticalLayout_2.addWidget(self.settings_button, 0, QtCore.Qt.AlignHCenter)
        self.exit_button = QtWidgets.QPushButton(self.main_menu)
        self.exit_button.setMinimumSize(QtCore.QSize(450, 100))
        self.exit_button.setMaximumSize(QtCore.QSize(450, 100))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(-1)
        self.exit_button.setFont(font)
        self.exit_button.setObjectName("exit_button")
        self.verticalLayout_2.addWidget(self.exit_button, 0, QtCore.Qt.AlignHCenter)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.main_stack.addWidget(self.main_menu)
        self.lobby = QtWidgets.QWidget()
        self.lobby.setObjectName("lobby")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.lobby)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lobby_list = QtWidgets.QListWidget(self.lobby)
        font = QtGui.QFont()
        font.setPointSize(40)
        self.lobby_list.setFont(font)
        self.lobby_list.setStyleSheet("             background-color: #ebc17a;\n"
"                border: 6px groove #d9a143")
        self.lobby_list.setObjectName("lobby_list")
        item = QtWidgets.QListWidgetItem()
        self.lobby_list.addItem(item)
        self.verticalLayout_5.addWidget(self.lobby_list)
        self.add_player_lobby = QtWidgets.QPushButton(self.lobby)
        self.add_player_lobby.setMinimumSize(QtCore.QSize(0, 50))
        self.add_player_lobby.setObjectName("pushButton_5")
        self.verticalLayout_5.addWidget(self.add_player_lobby)
        self.remove_player_lobby = QtWidgets.QPushButton(self.lobby)
        self.remove_player_lobby.setMinimumSize(QtCore.QSize(0, 50))
        self.remove_player_lobby.setObjectName("pushButton_4")
        self.verticalLayout_5.addWidget(self.remove_player_lobby)
        self.pushButton_6 = QtWidgets.QPushButton(self.lobby)
        self.pushButton_6.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_5.addWidget(self.pushButton_6)
        self.pushButton_3 = QtWidgets.QPushButton(self.lobby)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_5.addWidget(self.pushButton_3)
        self.verticalLayout_4.addLayout(self.verticalLayout_5)
        self.main_stack.addWidget(self.lobby)
        self.p_or_b = QtWidgets.QWidget()
        self.p_or_b.setObjectName("p_or_b")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.p_or_b)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.main_stack.addWidget(self.p_or_b)
        self.verticalLayout.addWidget(self.main_stack)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.retranslateUi(Form)
        self.main_stack.setCurrentIndex(0)
        self.exit_button.clicked.connect(Form.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.play_button.clicked.connect(self.open_login_window)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Poker and Blackjack", "Poker and Blackjack"))
        self.title.setText(_translate("Poker and Blackjack", "🅿🅾🅺🅴🆁 🅰🅽🅳 🅱🅻🅰🅲🅺🅹🅰🅲🅺"))
        self.play_button.setText(_translate("Poker and Blackjack", "Play"))
        self.settings_button.setText(_translate("Poker and Blackjack", "Settings"))
        self.exit_button.setText(_translate("Poker and Blackjack", "Exit"))
        __sortingEnabled = self.lobby_list.isSortingEnabled()
        self.lobby_list.setSortingEnabled(False)
        item = self.lobby_list.item(0)
        item.setText(_translate("Poker and Blackjack", "Player 1"))
        self.lobby_list.setSortingEnabled(__sortingEnabled)
        self.add_player_lobby.setText(_translate("Poker and Blackjack", "Add player"))
        self.remove_player_lobby.setText(_translate("Poker and Blackjack", "Remove player"))
        self.pushButton_6.setText(_translate("Poker and Blackjack", "Start lobby"))
        self.pushButton_3.setText(_translate("Poker and Blackjack", "Exit lobby"))


    def reset_lobby(self):
        self.lobby_table.clear()
        self.main_stack.setCurrentIndex(1)

    def open_login_window(self):
        self.window = QtWidgets.QDialog()
        self.ui = Login()
        self.ui.setupUi(self.window)
        self.ui.username_line.setText('Alex')
        self.ui.password_line.setText('alex')
        self.window.show()


if __name__ == '__main__':
    import sys
    import qt5reactor
    app = QtWidgets.QApplication(sys.argv)

    qt5reactor.install()

    main = QtWidgets.QWidget()
    ui = Menu()
    ui.setupUi(main)

    # create_login = Login()
    # create_game = CreateGame()
    import skel_client as tcp_client

    main.show()


    # Start TCP Client
    tcp_client.ClientCreator.start_connection()


    # main.show()

    sys.exit(app.exec_())


