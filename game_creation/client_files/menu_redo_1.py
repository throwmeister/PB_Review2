from PyQt5 import QtCore, QtGui, QtWidgets
from create_game_screen import CreateGame
from login_screen import Login
from join_game_screen import JoinGame
from client_data import ClientInfo, GameInfo
from game_creation.shared_directory import data_format as form


class Menu(object):
    def setupUi(self, Form):
        Form.setObjectName("Poker and Blackjack")
        Form.closeEvent = self.closed_event
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
        self.game_player_list = QtWidgets.QWidget()
        self.player_list_screen = QtWidgets.QWidget()
        self.player_list_screen.setObjectName("p_or_b")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.player_list_screen)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.player_list = QtWidgets.QListWidget(self.player_list_screen)
        self.player_list.setStyleSheet("background-color: #ebc17a;\n"
                                       "                border: 6px groove #d9a143;\n"
                                       "font-size: 22px;")
        self.player_list.setObjectName("player_list")
        self.verticalLayout_6.addWidget(self.player_list)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.start_game_button = QtWidgets.QPushButton(self.player_list_screen)
        self.start_game_button.setEnabled(False)
        self.start_game_button.setObjectName("start_game_button")
        self.horizontalLayout.addWidget(self.start_game_button)
        self.playing_checkbox = QtWidgets.QCheckBox(self.player_list_screen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playing_checkbox.sizePolicy().hasHeightForWidth())
        self.playing_checkbox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.playing_checkbox.setFont(font)
        self.playing_checkbox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.playing_checkbox.setStyleSheet("font-family: MS Shell Dlg 2;\n"
                                            "    font-size: 30px;\n"
                                            "                \n"
                                            "    color: rgb(0, 85, 0);\n"
                                            "                \n"
                                            "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 132, 93, 255), stop:1 rgba(97, 192, 164, 255));\n"
                                            "                border-radius: 3px;\n"
                                            "                border: 2px groove rgb(0, 0, 0)")
        self.playing_checkbox.setObjectName("playing_checkbox")
        self.horizontalLayout.addWidget(self.playing_checkbox)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.leave_game_button = QtWidgets.QPushButton(self.player_list_screen)
        self.leave_game_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.leave_game_button.setObjectName("leave_game_button")
        self.verticalLayout_6.addWidget(self.leave_game_button)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.main_stack.addWidget(self.player_list_screen)
        self.verticalLayout.addWidget(self.main_stack)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        # self.add_bet_stack()
        self.add_bet_stack()
        self.add_poker_stack()
        self.retranslateUi(Form)
        self.main_stack.setCurrentIndex(0)
        self.exit_button.clicked.connect(Form.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.play_button.clicked.connect(self.open_login_window)
        ClientInfo.main_gui = self

        self.refresh_bet_game()
        self.settings_button.clicked.connect(self.tester_button)
        self.games_list.itemClicked.connect(self.game_clicked)
        self.join_game_button.clicked.connect(self.join_game_pressed)
        self.create_game_button.clicked.connect(self.create_game_pressed)
        self.back_button_game_list.clicked.connect(lambda _: self.main_stack.setCurrentIndex(0))
        self.playing_checkbox.clicked.connect(self.playing_checkbox_clicked)
        self.start_game_button.clicked.connect(self.start_game_clicked)
        self.bet_button.clicked.connect(self.bet_button_pressed)
        self.bet_again_button.clicked.connect(self.bet_again_button_clicked)
        self.tester_button()

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
        self.games_list.setSortingEnabled(__sortingEnabled)
        self.join_game_button.setText(_translate("Form", "Join game"))
        self.create_game_button.setText(_translate("Form", "Create game"))
        self.back_button_game_list.setText(_translate("Form", "Back"))
        self.start_game_button.setText(_translate("Form", "Start"))
        self.playing_checkbox.setText(_translate("Form", "Playing"))
        self.leave_game_button.setText(_translate("Form", "Leave"))
        self.EMPTY.setText(_translate("Form", "EMPTY SPACE"))
        "self.make_bet_button.setText(_translate('Form', 'Make bet'))"
        self.replace_button.setText(_translate("Form", "Replace: 0"))
        self.fold_button.setText(_translate("Form", "Fold"))
        self.leave_ingame_button.setText(_translate("Form", "Leave Game"))
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

    def add_bet_stack(self):
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
        self.bank_counter_brown = QtWidgets.QLabel(self.bet_stack)
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
        self.bank_red_chip = Chips(self.bet_stack, self.chip_clicked, form.ChipType.RED)
        self.bank_red_chip.setMinimumSize(QtCore.QSize(100, 100))
        self.bank_red_chip.setMaximumSize(QtCore.QSize(100, 100))
        self.bank_red_chip.setText("")
        self.bank_red_chip.setPixmap(QtGui.QPixmap(self.red_chip_icon))
        self.bank_red_chip.setScaledContents(True)
        self.bank_red_chip.setObjectName("bank_red_chip")
        self.horizontalLayout_2.addWidget(self.bank_red_chip)
        self.bank_blue_chip = Chips(self.bet_stack, self.chip_clicked, form.ChipType.BLUE)
        self.bank_blue_chip.setMaximumSize(QtCore.QSize(100, 100))
        self.bank_blue_chip.setText("")
        self.bank_blue_chip.setPixmap(QtGui.QPixmap(self.blue_chip_icon))
        self.bank_blue_chip.setScaledContents(True)
        self.bank_blue_chip.setObjectName("bank_blue_chip")
        self.horizontalLayout_2.addWidget(self.bank_blue_chip)
        self.bank_brown_chip = Chips(self.bet_stack, self.chip_clicked, form.ChipType.BROWN)
        self.bank_brown_chip.setMaximumSize(QtCore.QSize(100, 100))
        self.bank_brown_chip.setText("")
        self.bank_brown_chip.setPixmap(QtGui.QPixmap(self.brown_chip_icon))
        self.bank_brown_chip.setScaledContents(True)
        self.bank_brown_chip.setObjectName("bank_brown_chip")
        self.horizontalLayout_2.addWidget(self.bank_brown_chip)
        self.bank_black_chip = Chips(self.bet_stack, self.chip_clicked, form.ChipType.BLACK)
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
        self.bet_red_chip = Chips(self.bet_stack, self.chip_clicked, form.ChipType.RED)
        self.bet_red_chip.setMinimumSize(QtCore.QSize(100, 100))
        self.bet_red_chip.setMaximumSize(QtCore.QSize(100, 100))
        self.bet_red_chip.setText("")
        self.bet_red_chip.setPixmap(QtGui.QPixmap(self.red_chip_icon))
        self.bet_red_chip.setScaledContents(True)
        self.bet_red_chip.setObjectName("bet_red_chip")
        self.bet_hz_bet_layout.addWidget(self.bet_red_chip)
        self.bet_blue_chip = Chips(self.bet_stack, self.chip_clicked, form.ChipType.BLUE)
        self.bet_blue_chip.setMaximumSize(QtCore.QSize(100, 100))
        self.bet_blue_chip.setText("")
        self.bet_blue_chip.setPixmap(QtGui.QPixmap(self.blue_chip_icon))
        self.bet_blue_chip.setScaledContents(True)
        self.bet_blue_chip.setObjectName("bet_blue_chip")
        self.bet_hz_bet_layout.addWidget(self.bet_blue_chip)
        self.bet_brown_chip = Chips(self.bet_stack, self.chip_clicked, form.ChipType.BROWN)
        self.bet_brown_chip.setMaximumSize(QtCore.QSize(100, 100))
        self.bet_brown_chip.setText("")
        self.bet_brown_chip.setPixmap(QtGui.QPixmap(self.brown_chip_icon))
        self.bet_brown_chip.setScaledContents(True)
        self.bet_brown_chip.setObjectName("bet_brown_chip")
        self.bet_hz_bet_layout.addWidget(self.bet_brown_chip)
        self.bet_black_chip = Chips(self.bet_stack, self.chip_clicked, form.ChipType.BLACK)
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

        self.chip_dict = TwoWayDict()

        self.chip_dict[self.bank_red_chip] = self.bet_red_chip
        self.chip_dict[self.bank_blue_chip] = self.bet_blue_chip
        self.chip_dict[self.bank_brown_chip] = self.bet_brown_chip
        self.chip_dict[self.bank_black_chip] = self.bet_black_chip

        # self.refresh_bet_game()

        self.main_stack.addWidget(self.bet_stack)

    def refresh_bet_game(self):
        self.bank_balance_var = 75
        self.bet_balance_var = 0
        _translate = QtCore.QCoreApplication.translate
        self.bank_balance.setText(_translate("Dialog", f"Balance: {self.bank_balance_var}"))
        self.bank_counter_red.setText(_translate("Dialog", "5"))
        self.bank_counter_blue.setText(_translate("Dialog", "5"))
        self.bank_counter_brown.setText(_translate("Dialog", "5"))
        self.bank_counter_black.setText(_translate("Dialog", "5"))
        self.bet_balance.setText(_translate("Dialog", f"Betting: {self.bank_balance_var}"))
        self.bet_counter_red.setText(_translate("Dialog", "0"))
        self.bet_counter_blue.setText(_translate("Dialog", "0"))
        self.bet_counter_brown.setText(_translate("Dialog", "0"))
        self.bet_counter_black.setText(_translate("Dialog", "0"))
        self.bank_red_chip.setup_chips(5)
        self.bank_blue_chip.setup_chips(5)
        self.bank_brown_chip.setup_chips(5)
        self.bank_black_chip.setup_chips(5)
        self.bet_red_chip.setup_chips(0)
        self.bet_blue_chip.setup_chips(0)
        self.bet_brown_chip.setup_chips(0)
        self.bet_black_chip.setup_chips(0)

        self.bank = [self.bank_red_chip, self.bank_blue_chip, self.bank_brown_chip, self.bank_black_chip]
        self.bet = [self.bet_red_chip, self.bet_blue_chip, self.bet_brown_chip, self.bet_black_chip]

        print('ran refresh')
        print(self.bank)
        print(self.bet)

    def chip_clicked(self, event, chip_obj):
        button = event.button()
        modifiers = event.modifiers()
        if modifiers == QtCore.Qt.NoModifier and button == QtCore.Qt.LeftButton:
            chip_obj: Chips
            bet_chip = self.chip_dict[chip_obj]
            print('got here')
            bet_chip: Chips
            if chip_obj.chips:
                chip = chip_obj.chips.pop()
                print(chip)
                bet_chip.add_chip(chip)
                self.update_chip_balance()

        elif modifiers == QtCore.Qt.NoModifier and button == QtCore.Qt.RightButton:
            print('wtf')


    '''
    def bet_chip_clicked(self, event, chip_obj):
        button = event.button()
        modifiers = event.modifiers()
        if modifiers == QtCore.Qt.NoModifier and button == QtCore.Qt.LeftButton:
            chip_obj: Chips
            bet_chip = self.chip_dict[chip_obj]
            bet_chip: Chips
            chip = chip_obj.chips.pop()
            bet_chip.add_chip(chip)
            self.update_chip_balance()
            '''

    def update_chip_balance(self):

        self.bank_balance_var = 0
        self.bet_balance_var = 0


        for bank in self.bank:
            for chip in bank.chips:
                chip: Chip
                self.bank_balance_var += chip.monetary_value

        for bet in self.bet:
            print(f'bet balance: {bet.chips}')
            for chip in bet.chips:
                chip: Chip
                self.bet_balance_var += chip.monetary_value

        self.bank_balance.setText(f"Balance: {self.bank_balance_var}")
        self.bet_balance.setText(f"Betting: {self.bet_balance_var}")
        self.bank_counter_red.setText(f'{self.bank[0].num_of_chips}')
        self.bank_counter_blue.setText(f'{self.bank[1].num_of_chips}')
        self.bank_counter_brown.setText(f'{self.bank[2].num_of_chips}')
        self.bank_counter_black.setText(f'{self.bank[3].num_of_chips}')
        self.bet_counter_red.setText(f'{self.bet[0].num_of_chips}')
        self.bet_counter_blue.setText(f'{self.bet[1].num_of_chips}')
        self.bet_counter_brown.setText(f'{self.bet[2].num_of_chips}')
        self.bet_counter_black.setText(f'{self.bet[3].num_of_chips}')

    def add_poker_stack(self):
        self.poker_screen = QtWidgets.QWidget()
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.poker_screen)
        self.verticalLayout_22.setObjectName("verticalLayout_2")
        self.verticalLayout23 = QtWidgets.QVBoxLayout()
        self.verticalLayout23.setObjectName("verticalLayout")
        self.EMPTY = QtWidgets.QLabel(self.poker_screen)
        self.EMPTY.setAlignment(QtCore.Qt.AlignCenter)
        self.EMPTY.setObjectName("label")
        self.verticalLayout23.addWidget(self.EMPTY)
        self.horizontalLayout22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout22.setObjectName("horizontalLayout")
        self.card1 = ExtendedCard(self.poker_screen, self.card_clicked)
        self.card1.setMinimumSize(QtCore.QSize(200, 100))
        self.card1.setMaximumSize(QtCore.QSize(200, 300))
        self.card1.setText("")
        self.back_card = "images/back_card.png"
        self.card1.setPixmap(QtGui.QPixmap(self.back_card))
        self.card1.setScaledContents(True)
        self.card1.setObjectName("label_4")
        self.horizontalLayout22.addWidget(self.card1, 0, QtCore.Qt.AlignVCenter)
        self.card2 = ExtendedCard(self.poker_screen, self.card_clicked)
        self.card2.setMaximumSize(QtCore.QSize(200, 300))
        self.card2.setText("")
        self.card2.setPixmap(QtGui.QPixmap(self.back_card))
        self.card2.setScaledContents(True)
        self.card2.setObjectName("label_3")
        self.horizontalLayout22.addWidget(self.card2, 0, QtCore.Qt.AlignVCenter)
        self.card3 = ExtendedCard(self.poker_screen, self.card_clicked)
        self.card3.setMaximumSize(QtCore.QSize(200, 300))
        self.card3.setText("")
        self.card3.setPixmap(QtGui.QPixmap(self.back_card))
        self.card3.setScaledContents(True)
        self.card3.setObjectName("label_6")
        self.horizontalLayout22.addWidget(self.card3, 0, QtCore.Qt.AlignVCenter)
        self.card4 = ExtendedCard(self.poker_screen, self.card_clicked)
        self.card4.setMaximumSize(QtCore.QSize(200, 300))
        self.card4.setText("")
        self.card4.setPixmap(QtGui.QPixmap(self.back_card))
        self.card4.setScaledContents(True)
        self.card4.setObjectName("label_5")
        self.horizontalLayout22.addWidget(self.card4, 0, QtCore.Qt.AlignVCenter)
        self.card5 = ExtendedCard(self.poker_screen, self.card_clicked)
        self.card5.setMaximumSize(QtCore.QSize(200, 300))
        self.card5.setText("")
        self.card5.setPixmap(QtGui.QPixmap(self.back_card))
        self.card5.setScaledContents(True)
        self.card5.setObjectName("label_2")
        self.horizontalLayout22.addWidget(self.card5, 0, QtCore.Qt.AlignVCenter)
        self.verticalLayout23.addLayout(self.horizontalLayout22)
        '''
        self.make_bet_button = QtWidgets.QPushButton(self.game_screen)
        self.verticalLayout23.addWidget(self.make_bet_button)
        '''
        self.replace_button = QtWidgets.QPushButton(self.poker_screen)
        self.replace_button.setObjectName("pushButton_3")
        self.verticalLayout23.addWidget(self.replace_button)
        self.bet_again_button = QtWidgets.QPushButton(self.poker_screen)
        self.bet_again_button.setDisabled(True)
        self.verticalLayout23.addWidget(self.bet_again_button)
        self.fold_button = QtWidgets.QPushButton(self.poker_screen)
        self.fold_button.setObjectName("pushButton")
        self.verticalLayout23.addWidget(self.fold_button)
        self.leave_ingame_button = QtWidgets.QPushButton(self.poker_screen)
        self.leave_ingame_button.setObjectName("pushButton_2")
        self.verticalLayout23.addWidget(self.leave_ingame_button)
        self.verticalLayout_22.addLayout(self.verticalLayout23)

        self.main_stack.addWidget(self.poker_screen)

        self.card_list = [self.card1, self.card2, self.card3, self.card4, self.card5]
        GameInfo.state = form.GameState.BETTING

        # self.replace_button.setDisabled(True)

        self.replace_button.clicked.connect(self.replace_button_clicked)

    def refresh_poker_screen(self):
        self.card1.setPixmap(QtGui.QPixmap(self.back_card))
        self.card2.setPixmap(QtGui.QPixmap(self.back_card))
        self.card3.setPixmap(QtGui.QPixmap(self.back_card))
        self.card4.setPixmap(QtGui.QPixmap(self.back_card))
        self.card5.setPixmap(QtGui.QPixmap(self.back_card))

    def add_blackjack_stack(self):
        self.blackjack_screen = QtWidgets.QWidget()

        self.main_stack.addWidget(self.blackjack_screen)

    def refresh_bj_screen(self):
        pass

    def add_winner_screen(self):
        self.winner_screen = QtWidgets.QWidget()

    def signal(self):
        ClientInfo.tcpHandler.request_start_signal()

    def card_clicked(self, event, card_obj):
        button = event.button()
        modifiers = event.modifiers()
        if modifiers == QtCore.Qt.NoModifier and button == QtCore.Qt.LeftButton:
            card_obj: ExtendedCard
            if GameInfo.state == form.GameState.CARD_CHANGING:
                if card_obj.selected:
                    ClientInfo.logger.info('Deselecting')
                    card_obj.deselect_card()
                else:
                    ClientInfo.logger.info('Selecting')
                    card_obj.select_card()
                    if len(GameInfo.replace_list) == 4:
                        removed_card = GameInfo.replace_list[0]
                        removed_card: ExtendedCard
                        removed_card.deselect_card()
                self.replace_button.setText(f'Replace: {len(GameInfo.replace_list)}')

    def set_cards(self, cards):
        ClientInfo.logger.info(cards)
        for i, card in enumerate(cards):
            ClientInfo.logger.info(card)
            c = form.ExtractCard(card)
            self.card_list[i].set_values(c.suit, c.value)

    def replace_button_clicked(self):
        self.replace_button.setDisabled(True)
        cards = []
        ClientInfo.logger.info(f'Current replace list: {GameInfo.replace_list}')
        for card in GameInfo.replace_list:
            card.setStyleSheet('')
            card: ExtendedCard
            d = form.ExtractCard()
            d.suit = card.suit
            d.value = card.value
            cards.append(d.__dict__)
        ClientInfo.logger.info(f'Cards being replaced: {cards}')
        ClientInfo.tcpHandler.send_replace_cards(cards)

    def tester_button(self):
        self.main_stack.setCurrentIndex(3)

    def game_clicked(self, items):
        '''
        print(self.games_list.topLevelItem(0).data(5, 0))
        print(self.games_list.selectedItems()[0])
        print(items.treeWidget().currentIndex().row())'''
        self.selected_game = items.data(5, 0)
        print(self.selected_game)

    def change_screens(self, num):
        self.main_stack.setCurrentIndex(int(num))

    def open_login_window(self):
        if ClientInfo.valid_session:
            self.change_screens(form.MenuScreenEnums.GAME_LIST)
        else:
            self.lwindow = QtWidgets.QDialog()
            self.lui = Login()
            self.lui.setupUi(self.lwindow)
            self.lui.username_line.setText('Alex')
            self.lui.password_line.setText('alex')
            self.lwindow.show()
            print('This ran!')

    def set_game_list(self, data):
        self.games_list.clear()
        ClientInfo.logger.info(data)
        try:
            for game_id, game_vars in data.items():
                ClientInfo.logger.info(f'Game from game_id: {game_id} and values: {game_vars}')
                d = form.UpdateGameListVariables(game_vars)
                items = [d.game_name, d.game_type, d.owner, str(d.num_players), str(d.in_progress), game_id]
                QtWidgets.QTreeWidgetItem(self.games_list, items)
        except AttributeError:
            pass

    def set_player_list(self, data):
        self.player_list.clear()
        ClientInfo.logger.info('Setting game player list')
        ClientInfo.logger.info(data)
        for player in data:
            d = form.UpdatePlayerList(player)
            ready = '✅'
            if d.ready == form.PlayerReadyEnum.FALSE:
                ready = '❌'
            self.player_list.addItem(f'{d.player_name} {ready}')

    def join_game_pressed(self):
        if self.selected_game:
            self.jwindow = QtWidgets.QDialog()
            self.jui = JoinGame()
            self.jui.setupUi(self.jwindow)
            self.jui.game_id = self.selected_game
            self.jui.password_edit.setText('ILOVEPOKER')
            self.jwindow.show()
        else:
            print('please select a game')

    def create_game_pressed(self):
        self.create_window = QtWidgets.QDialog()
        self.create_ui = CreateGame()
        self.create_ui.setupUi(self.create_window)
        self.create_window.show()

    def set_owner_command(self):
        self.start_game_button.setEnabled(True)

    def playing_checkbox_clicked(self):
        self.playing_checkbox.setEnabled(False)
        if self.playing_checkbox.isChecked():
            ClientInfo.tcpHandler.ready_game(game_id=ClientInfo.game_id, ready_type=form.ReadyTypeEnum.READY)
        else:
            ClientInfo.tcpHandler.ready_game(game_id=ClientInfo.game_id, ready_type=form.ReadyTypeEnum.UNREADY)

    def ready_success(self):
        ClientInfo.logger.info('Ready: success')
        self.playing_checkbox.setEnabled(True)

    def ready_error(self, reverse_action: bool):
        self.playing_checkbox.setEnabled(True)
        self.playing_checkbox.setChecked(reverse_action)
        ClientInfo.logger.info('Ready failed')

    def start_game_clicked(self):
        ClientInfo.tcpHandler.start_game()

    def setup_game(self, gtype):
        ClientInfo.logger.info('Setting up game')
        GameInfo.set_initial_values(gtype)
        self.refresh_bet_screen()
        self.change_screens(form.MenuScreenEnums.BET_SCREEN)
        GameInfo.state = form.GameState.BETTING
        ClientInfo.logger.info('Opening bet screen...')

    def refresh_bet_screen(self):
        self.bet_edit.setText("")
        self.amount_label.setText(f'Amount: {GameInfo.bet}')
        self.bet_button.setEnabled(True)


    def bet_button_pressed(self):
        self.bet_button.setDisabled(True)
        try:
            self.amount = int(self.bet_edit.text())
            if 0 <= self.amount < GameInfo.bet:
                ClientInfo.logger.info('Sending bet amount')
                ClientInfo.tcpHandler.send_bet(self.amount)
            else:
                self.bet_button.setDisabled(False)
                ClientInfo.logger.error('Invalid amount')
        except ValueError:
            self.bet_button.setDisabled(False)
            ClientInfo.logger.error('Invalid character')

    def bet_success(self):
        GameInfo.bet -= self.amount
        ClientInfo.tcpHandler.request_cards()
        if GameInfo.game_type == form.GameTypeEnum.POKER:
            self.refresh_poker_screen()
            self.change_screens(form.MenuScreenEnums.POKER_SCREEN)
        elif GameInfo.game_type == form.GameTypeEnum.BLACKJACK:
            self.refresh_bj_screen()
            self.change_screens(form.MenuScreenEnums.BLACKJACK_SCREEN)

    def all_bets_done(self):
        # Prompt
        GameInfo.state = form.GameState.CARD_CHANGING

    def enable_second_bet(self):
        self.bet_again_button.setEnabled(True)
        self.refresh_bet_screen()

    def bet_error(self):
        ClientInfo.logger.info('Bet error')
        self.bet_button.setDisabled(False)

    def bet_again_button_clicked(self):
        self.bet_again_button.setDisabled(True)
        self.change_screens(form.MenuScreenEnums.BET_SCREEN)

    def handle_won(self, amount):
        pass

    def closed_event(self, event):
        ClientInfo.tcpHandler.lose_connection()
        raise RuntimeError


class ExtendedCard(QtWidgets.QLabel):
    selected_style_sheet = '''background-color: #ebc17a;
                border: 6px groove #d9a143;'''

    def __init__(self, form, func):
        super(ExtendedCard, self).__init__(form)
        self.suit = ''
        self.value = 0
        self.when_clicked = func
        self.selected = False

    def set_values(self, suit, value):
        self.suit = suit
        self.value = value
        self.setPixmap(QtGui.QPixmap(f'images/PNG-cards-1.3/{value}_of_{suit.lower()}.png'))

    def mouseReleaseEvent(self, ev):
        self.when_clicked(ev, self)

    def select_card(self):
        self.selected = True
        self.setStyleSheet(self.selected_style_sheet)
        GameInfo.replace_list.append(self)

    def deselect_card(self):
        self.selected = False
        self.setStyleSheet('')
        try:
            GameInfo.replace_list.remove(self)
        except ValueError:
            pass


class Chip:
    def __init__(self, val):
        self.monetary_value = val


class Chips(QtWidgets.QLabel):
    def __init__(self, form, clicked_func, chip_type):
        super(Chips, self).__init__(form)
        self.chips = []
        self.chip_type = chip_type
        self.when_clicked = clicked_func

    def mouseReleaseEvent(self, ev):
        self.when_clicked(ev, self)

    @property
    def num_of_chips(self):
        return len(self.chips)

    def setup_chips(self, num):
        self.chips = []
        for _ in range(num):
            self.chips.append(Chip(self.chip_type))

    def add_chip(self, chip):
        self.chips.append(chip)


class TwoWayDict(dict):
    def __len__(self):
        return dict.__len__(self) / 2

    def __setitem__(self, key, value):
        dict.__setitem__(self, key, value)
        dict.__setitem__(self, value, key)


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

    sys.exit(app.exec_())
