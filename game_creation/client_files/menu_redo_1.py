from PyQt5 import QtCore, QtGui, QtWidgets
from create_game_screen import CreateGame
from login_screen import Login
from join_game_screen import JoinGame
from poker_game_screen import Game
from client_data import ClientInfo, GameInfo
from bet_screen import Bet
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
        self.add_bet_stack()
        self.add_poker_stack()
        self.retranslateUi(Form)
        self.main_stack.setCurrentIndex(0)
        self.exit_button.clicked.connect(Form.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.play_button.clicked.connect(self.open_login_window)
        ClientInfo.main_gui = self
        self.settings_button.clicked.connect(self.tester_button)
        self.games_list.itemClicked.connect(self.game_clicked)
        self.join_game_button.clicked.connect(self.join_game_pressed)
        self.create_game_button.clicked.connect(self.create_game_pressed)
        self.back_button_game_list.clicked.connect(lambda _: self.main_stack.setCurrentIndex(0))
        self.playing_checkbox.clicked.connect(self.playing_checkbox_clicked)
        self.start_game_button.clicked.connect(self.start_game_clicked)
        self.bet_button.clicked.connect(self.bet_button_pressed)
        # self.tester_button()

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

        self.bet_label.setText(_translate("Dialog", "Bet amount: "))
        self.amount_label.setText(_translate("Dialog", f"Amount: {GameInfo.bet}"))
        self.bet_button.setText(_translate("Dialog", "Bet"))

    def add_bet_stack(self):
        self.bet_screen = QtWidgets.QWidget()
        self.bet_vert_layout = QtWidgets.QVBoxLayout(self.bet_screen)
        self.bet_vert_layout.setObjectName("verticalLayout_2")
        self.bet_vert_layout0 = QtWidgets.QVBoxLayout()
        self.bet_vert_layout0.setObjectName("verticalLayout")
        self.bet_label = QtWidgets.QLabel(self.bet_screen)
        self.bet_label.setMaximumSize(QtCore.QSize(400, 50))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(-1)
        self.bet_label.setFont(font)
        self.bet_label_style = '''font-family: MS Shell Dlg 2;\n
                                         font-size: 30px;'''
        self.bet_label.setStyleSheet(self.bet_label_style)
        self.bet_label.setObjectName("label")
        self.bet_vert_layout0.addWidget(self.bet_label, 0, QtCore.Qt.AlignHCenter)
        self.bet_form_layout = QtWidgets.QFormLayout()
        self.bet_form_layout.setObjectName("formLayout")
        self.amount_label = QtWidgets.QLabel(self.bet_screen)
        self.amount_label.setStyleSheet(self.bet_label_style)
        self.amount_label.setObjectName("label_3")
        self.bet_form_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.amount_label)
        self.bet_edit = QtWidgets.QLineEdit(self.bet_screen)
        self.bet_edit.setStyleSheet(self.bet_label_style)
        self.bet_edit.setMinimumSize(QtCore.QSize(0, 50))
        self.bet_edit.setText("")
        self.bet_edit.setClearButtonEnabled(False)
        self.bet_edit.setObjectName("lineEdit_2")
        self.bet_form_layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.bet_edit)
        self.bet_vert_layout0.addLayout(self.bet_form_layout)
        self.bet_vert_layout.addLayout(self.bet_vert_layout0)
        self.bet_button = QtWidgets.QPushButton(self.bet_screen)
        self.bet_button.setObjectName("pushButton")
        self.bet_vert_layout.addWidget(self.bet_button)

        self.main_stack.addWidget(self.bet_screen)



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

    def signal(self):
        ClientInfo.tcpHandler.request_start_signal()

    def card_clicked(self, event, card_obj):
        button = event.button()
        modifiers = event.modifiers()
        print('ran')
        if modifiers == QtCore.Qt.NoModifier and button == QtCore.Qt.LeftButton:
            print('ran 2')
            card_obj: ExtendedCard
            if GameInfo.state == form.GameState.CARD_CHANGING:
                print('ice')
                if card_obj.selected:
                    # ClientInfo.logger.info('Deselecting')
                    card_obj.deselect_card()
                else:
                    # ClientInfo.logger.info('Selecting')
                    card_obj.select_card()
                    if len(GameInfo.replace_list) == 4:
                        removed_card = GameInfo.replace_list[0]
                        removed_card: ExtendedCard
                        removed_card.deselect_card()
                self.replace_button.setText(f'Replace: {len(GameInfo.replace_list)}')

    def open_bet_screen(self):
        self.lwindow = QtWidgets.QDialog()
        self.lui = Bet()
        self.lui.setupUi(self.lwindow)
        self.lwindow.show()
        GameInfo.state = form.GameState.CARD_CHANGING

    def set_cards(self, cards):
        ClientInfo.logger.info(cards)
        for i, card in enumerate(cards):
            ClientInfo.logger.info(card)
            c = form.ExtractCard(card)
            self.card_list[i].set_values(c.suit, c.value)

    def replace_button_clicked(self):
        self.replace_button.setDisabled(True)
        cards = []
        for card in GameInfo.replace_list:
            card: ExtendedCard
            d = form.ExtractCard()
            d.suit = card.suit
            d.value = card.value
            print(d.__dict__)
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

    def refresh_game_screen(self):
        pass

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


    def bet_error(self):
        ClientInfo.logger.info('Bet error')
        self.bet_button.setDisabled(False)


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
        GameInfo.replace_list.remove(self)
        self.setStyleSheet('')



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
