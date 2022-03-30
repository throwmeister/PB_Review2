from PyQt5 import QtCore, QtGui, QtWidgets
from create_game_screen import CreateGame
from login_screen import Login
from client_data import ClientInfo
from game_creation.shared_directory import data_format as form


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
"            }"
"QHeaderView::section {\n"
"    background-color: #ebc17a;\n"
"    border-style: none;\n"
"    font-size: 14pt;\n"
"    border-right: 1px solid #d9a143;\n"
"border-bottom: 1px solid #d9a143;\n"
"border-left: 1px solid #d9a143;\n"
"padding: 6px\n"
"}\n"
"QTableCornerButton::section{\n"
"background-color: #ebc17a;\n"
"    padding: 4px;\n"
"    border: 1px solid #ebc17a;\n"
"    font-size: 14pt;\n"
"}\n"
"\n"
"")
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
        self.games_list = QtWidgets.QTreeWidget(self.lobby)
        self.games_list.setStyleSheet("background-color: #ebc17a;\n"
                                      "                border: 6px groove #d9a143;\n"
                                      "font-size: 22px;\n"
                                      "QHeaderView::section\n"
                                      "{\n"
                                      "    border-top: 1px solid #fffff8;\n"
                                      "}\n"
                                      "\n"
                                      "QHeaderView::vertical\n"
                                      "{\n"
                                      "    border-left: 1px solid #fffff8;\n"
                                      "}")
        self.games_list.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.games_list)
        self.verticalLayout_5.addWidget(self.games_list)
        self.join_game_button = QtWidgets.QPushButton(self.lobby)
        self.join_game_button.setMinimumSize(QtCore.QSize(0, 50))
        self.join_game_button.setObjectName("pushButton_5")
        self.verticalLayout_5.addWidget(self.join_game_button)
        self.create_game_button = QtWidgets.QPushButton(self.lobby)
        self.create_game_button.setMinimumSize(QtCore.QSize(0, 50))
        self.create_game_button.setObjectName("pushButton_4")
        self.verticalLayout_5.addWidget(self.create_game_button)
        self.back_button_game_list = QtWidgets.QPushButton(self.lobby)
        self.back_button_game_list.setMinimumSize(QtCore.QSize(0, 50))
        self.back_button_game_list.setObjectName("pushButton_3")
        self.verticalLayout_5.addWidget(self.back_button_game_list)
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
        ClientInfo.main_gui = self
        self.settings_button.clicked.connect(self.tester_button)
        self.games_list.itemClicked.connect(self.tester_func)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Poker and Blackjack", "Poker and Blackjack"))
        self.title.setText(_translate("Poker and Blackjack", "🅿🅾🅺🅴🆁 🅰🅽🅳 🅱🅻🅰🅲🅺🅹🅰🅲🅺"))
        self.play_button.setText(_translate("Poker and Blackjack", "Play"))
        self.settings_button.setText(_translate("Poker and Blackjack", "Settings"))
        self.exit_button.setText(_translate("Poker and Blackjack", "Exit"))
        self.games_list.headerItem().setText(0, _translate("Form", "Name"))
        self.games_list.headerItem().setText(1, _translate("Form", "Type"))
        self.games_list.headerItem().setText(2, _translate("Form", "Owner"))
        self.games_list.headerItem().setText(3, _translate("Form", "Players"))
        self.games_list.headerItem().setText(4, _translate("Form", "In progress"))
        __sortingEnabled = self.games_list.isSortingEnabled()
        self.games_list.setSortingEnabled(False)
        self.games_list.topLevelItem(0).setText(0, _translate("Form", "deez uts"))
        self.games_list.topLevelItem(0).setText(1, _translate("Form", "Poker"))
        self.games_list.topLevelItem(0).setText(2, _translate("Form", "GAB"))
        self.games_list.topLevelItem(0).setText(3, _translate("Form", "3"))
        self.games_list.topLevelItem(0).setText(4, _translate("Form", "False"))

        self.games_list.setSortingEnabled(__sortingEnabled)
        self.join_game_button.setText(_translate("Form", "Join game"))
        self.create_game_button.setText(_translate("Form", "Create game"))
        self.back_button_game_list.setText(_translate("Form", "Back"))

    def tester_button(self):
        self.main_stack.setCurrentIndex(1)
        items = ['Alex', 'Poker', 'alex', '1', 'False', 'Hi']
        QtWidgets.QTreeWidgetItem(self.games_list, items)

    def tester_func(self, items):
        '''
        print(self.games_list.topLevelItem(0).data(5, 0))
        print(self.games_list.selectedItems()[0])
        print(items.treeWidget().currentIndex().row())'''
        pass



    def change_to_games_screen(self):
        self.main_stack.setCurrentIndex(1)

    def open_login_window(self):
        self.window = QtWidgets.QDialog()
        self.ui = Login()
        self.ui.setupUi(self.window)
        self.ui.username_line.setText('Alex')
        self.ui.password_line.setText('alex')
        self.window.show()
        print('This ran!')

    def set_game_list(self, data):
        self.games_list.clear()
        for game_id, game_vars in data.items():
            ClientInfo.logger.info(f'Game from game_id: {game_id} and values: {game_vars}')
            d = form.UpdateGameListVariables(game_vars)
            items = [d.game_name, d.game_type, d.owner, str(d.num_players), str(d.in_progress), game_id]
            QtWidgets.QTreeWidgetItem(self.games_list, items)


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


