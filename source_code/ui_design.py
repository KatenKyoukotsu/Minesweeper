from PyQt5 import QtCore, QtGui, QtWidgets
from global_variables import MAIN_SIZES, MAIN_PATHS


def btn_pressed_toggle(path):
    a = path.split('.')
    if a[0].endswith('_pressed'):
        return f'{a[0][:-8]}.{a[1]}'
    return f'{a[0]}_pressed.{a[1]}'


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(956, 571)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.Box)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scrollArea.setLineWidth(4)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setStyleSheet("QWidget {background-color: rgb(200, 200, 200)}")
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 940, 514))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
        self.frame.setMinimumSize(QtCore.QSize(0, 0))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setLineWidth(4)
        self.frame.setObjectName("frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_5.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        conditions = ['switch_field_mode_beginner', 'switch_field_mode_amateur',
                      'switch_field_mode_professional', 'switch_field_mode_superman']
        self.switch_field_mode = ConditionButton(current_path=MAIN_PATHS['switch_field_mode_beginner'],
                                                 condition=0,
                                                 conditions=conditions)
        self.switch_field_mode.setMinimumSize(QtCore.QSize(*MAIN_SIZES['main_btn']))
        self.switch_field_mode.setMaximumSize(QtCore.QSize(*MAIN_SIZES['main_btn']))
        self.switch_field_mode.setText("")
        self.switch_field_mode.setObjectName("switch_field_mode")
        self.main_btns_group = QtWidgets.QButtonGroup(MainWindow)
        self.main_btns_group.setObjectName("main_btns_group")
        self.main_btns_group.addButton(self.switch_field_mode)
        self.horizontalLayout_2.addWidget(self.switch_field_mode)
        conditions = ['switch_click_mode_first', 'switch_click_mode_second']
        self.switch_click_mode = ConditionButton(current_path=MAIN_PATHS['switch_click_mode_first'],
                                                 condition=0,
                                                 conditions=conditions)
        self.switch_click_mode.setMinimumSize(QtCore.QSize(*MAIN_SIZES['main_btn']))
        self.switch_click_mode.setMaximumSize(QtCore.QSize(*MAIN_SIZES['main_btn']))
        self.switch_click_mode.setText("")
        self.switch_click_mode.setObjectName("switch_click_mode")
        self.main_btns_group.addButton(self.switch_click_mode)
        self.horizontalLayout_2.addWidget(self.switch_click_mode)
        conditions = ['switch_game_mode_random', 'switch_game_mode_safety']
        self.switch_game_mode = ConditionButton(current_path=MAIN_PATHS['switch_game_mode_random'],
                                                condition=0,
                                                conditions=conditions)
        self.switch_game_mode.setMinimumSize(QtCore.QSize(*MAIN_SIZES['main_btn']))
        self.switch_game_mode.setMaximumSize(QtCore.QSize(*MAIN_SIZES['main_btn']))
        self.switch_game_mode.setText("")
        self.switch_game_mode.setObjectName("switch_game_mode")
        self.main_btns_group.addButton(self.switch_game_mode)
        self.horizontalLayout_2.addWidget(self.switch_game_mode)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.main_text = QtWidgets.QLabel(self.frame)
        self.main_text.setMaximumSize(QtCore.QSize(185, 16777215))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(20)
        self.main_text.setFont(font)
        self.main_text.setObjectName("main_text")
        self.horizontalLayout_3.addWidget(self.main_text)
        self.app_icon = QtWidgets.QLabel(self.frame)
        self.app_icon.setMinimumSize(QtCore.QSize(32, 32))
        self.app_icon.setMaximumSize(QtCore.QSize(32, 32))
        self.app_icon.setText("")
        self.app_icon.setObjectName("app_icon")
        self.horizontalLayout_3.addWidget(self.app_icon)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_2.setLineWidth(4)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_6.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem4 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.lcd_count_mines = QtWidgets.QLCDNumber(self.frame_2)
        self.lcd_count_mines.setMinimumSize(QtCore.QSize(77, 49))
        self.lcd_count_mines.setMaximumSize(QtCore.QSize(77, 49))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lcd_count_mines.setFont(font)
        self.lcd_count_mines.setFrameShape(QtWidgets.QFrame.Box)
        self.lcd_count_mines.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcd_count_mines.setLineWidth(2)
        self.lcd_count_mines.setMidLineWidth(1)
        self.lcd_count_mines.setDigitCount(3)
        self.lcd_count_mines.setObjectName("lcd_count_mines")
        self.horizontalLayout.addWidget(self.lcd_count_mines)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.btn_smile = SmileButton(current_path=MAIN_PATHS['btn_smile_happy'])
        self.btn_smile.setMinimumSize(QtCore.QSize(*MAIN_SIZES['main_btn']))
        self.btn_smile.setMaximumSize(QtCore.QSize(*MAIN_SIZES['main_btn']))
        self.btn_smile.setText("")
        self.btn_smile.setObjectName("btn_smile")
        self.main_btns_group.addButton(self.btn_smile)
        self.horizontalLayout.addWidget(self.btn_smile)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.lcd_current_time = QtWidgets.QLCDNumber(self.frame_2)
        self.lcd_current_time.setMinimumSize(QtCore.QSize(77, 49))
        self.lcd_current_time.setMaximumSize(QtCore.QSize(77, 49))
        self.lcd_current_time.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lcd_current_time.setFont(font)
        self.lcd_current_time.setMouseTracking(False)
        self.lcd_current_time.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lcd_current_time.setAutoFillBackground(False)
        self.lcd_current_time.setFrameShape(QtWidgets.QFrame.Box)
        self.lcd_current_time.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcd_current_time.setLineWidth(2)
        self.lcd_current_time.setMidLineWidth(1)
        self.lcd_current_time.setDigitCount(3)
        self.lcd_current_time.setObjectName("lcd_current_time")
        self.horizontalLayout.addWidget(self.lcd_current_time)
        spacerItem7 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.horizontalLayout_6.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.frame_2)
        spacerItem8 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem8)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem9)
        self.frame_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_3.setLineWidth(4)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_7.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.gridLayout_field = QtWidgets.QGridLayout()
        self.gridLayout_field.setHorizontalSpacing(0)
        self.gridLayout_field.setObjectName("gridLayout_field")
        self.horizontalLayout_7.addLayout(self.gridLayout_field)
        self.horizontalLayout_4.addWidget(self.frame_3)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem10)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem11 = QtWidgets.QSpacerItem(20, 215, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem11)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout_2.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 956, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Сапёр"))
        self.main_text.setText(_translate("MainWindow", "Mi ne Sweeper"))


class DefaultButton(QtWidgets.QPushButton):
    def __init__(self, current_path=None, condition=None):
        super().__init__()
        self.setIcon(QtGui.QIcon(current_path))
        self.setIconSize(QtCore.QSize(*MAIN_SIZES['main_btn']))
        self.setStyleSheet('QPushButton {border: none;}')
        self.current_path = current_path
        self.condition = condition

    def update_current_path(self, path):
        self.current_path = path

    def change_btn(self):
        self.setIcon(QtGui.QIcon(self.current_path))

    def get_condition(self):
        return self.condition

    def get_toggle_press(self):
        self.update_current_path(btn_pressed_toggle(self.current_path))


class ConditionButton(DefaultButton):
    def __init__(self, current_path=None, condition=None, conditions=None):
        self.conditions = conditions
        super().__init__(current_path, condition)

    def change_condition(self):
        if type(self.condition) == int:
            self.condition += 1
            self.condition %= len(self.conditions)
            self.update_current_path(MAIN_PATHS[self.conditions[self.condition]])
            self.get_toggle_press()


class SmileButton(DefaultButton):
    def make_surprised(self):
        self.update_current_path(MAIN_PATHS["btn_smile_surprised"])

    def make_died(self):
        self.update_current_path(MAIN_PATHS["btn_smile_died"])

    def make_happy(self):
        self.update_current_path(MAIN_PATHS["btn_smile_happy"])

    def make_win(self):
        self.update_current_path(MAIN_PATHS["btn_smile_win"])