# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sidebar.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(965, 661)
        MainWindow.setStyleSheet("background-color: rgb(245, 250, 254);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(-1, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.icon_only_widget = QtWidgets.QWidget(self.centralwidget)
        self.icon_only_widget.setStyleSheet("QWidget{\n"
"background-color: rgb(31, 149, 239);\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"color:white;\n"
"border:none;\n"
"height:32px;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color:#F5FAFE;\n"
"color:#1F95EF;\n"
"font-weight:bold;\n"
"}")
        self.icon_only_widget.setObjectName("icon_only_widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 15, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.icon_only_widget)
        self.label.setMinimumSize(QtCore.QSize(40, 40))
        self.label.setMaximumSize(QtCore.QSize(40, 40))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/profile_pic.png"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 15, -1, -1)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dashboard_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.dashboard_1.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/dashboard_white.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/dashboard.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.dashboard_1.setIcon(icon)
        self.dashboard_1.setCheckable(True)
        self.dashboard_1.setAutoExclusive(True)
        self.dashboard_1.setObjectName("dashboard_1")
        self.verticalLayout.addWidget(self.dashboard_1)
        self.profile_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.profile_1.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/profile_white.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(":/profile.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.profile_1.setIcon(icon1)
        self.profile_1.setCheckable(True)
        self.profile_1.setAutoExclusive(True)
        self.profile_1.setObjectName("profile_1")
        self.verticalLayout.addWidget(self.profile_1)
        self.messages_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.messages_1.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/messages_white.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap(":/messages.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.messages_1.setIcon(icon2)
        self.messages_1.setCheckable(True)
        self.messages_1.setAutoExclusive(True)
        self.messages_1.setObjectName("messages_1")
        self.verticalLayout.addWidget(self.messages_1)
        self.notifications_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.notifications_1.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/notifications_white.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon3.addPixmap(QtGui.QPixmap(":/notifications.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.notifications_1.setIcon(icon3)
        self.notifications_1.setCheckable(True)
        self.notifications_1.setAutoExclusive(True)
        self.notifications_1.setObjectName("notifications_1")
        self.verticalLayout.addWidget(self.notifications_1)
        self.settings_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.settings_1.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/settings_white.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon4.addPixmap(QtGui.QPixmap(":/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.settings_1.setIcon(icon4)
        self.settings_1.setCheckable(True)
        self.settings_1.setAutoExclusive(True)
        self.settings_1.setObjectName("settings_1")
        self.verticalLayout.addWidget(self.settings_1)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 266, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.pushButton_6 = QtWidgets.QPushButton(self.icon_only_widget)
        self.pushButton_6.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/log_out_white.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon5)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_3.addWidget(self.pushButton_6)
        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)
        self.icon_name_widget = QtWidgets.QWidget(self.centralwidget)
        self.icon_name_widget.setStyleSheet("QWidget{\n"
"background-color: rgb(31, 149, 239);\n"
"color:white;\n"
"}\n"
"\n"
"QPushButton{\n"
"color:white;\n"
"text-align:left;\n"
"height:32px;\n"
"border:none;\n"
"padding-left:10px;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color:#F5FAFE;\n"
"color:#1F95EF;\n"
"font-weight:bold;\n"
"}")
        self.icon_name_widget.setObjectName("icon_name_widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.icon_name_widget)
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 15, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.icon_name_widget)
        self.label_2.setMinimumSize(QtCore.QSize(40, 40))
        self.label_2.setMaximumSize(QtCore.QSize(40, 40))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/profile_pic.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.icon_name_widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, 15, -1, -1)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.dashboard_2 = QtWidgets.QPushButton(self.icon_name_widget)
        self.dashboard_2.setIcon(icon)
        self.dashboard_2.setCheckable(True)
        self.dashboard_2.setAutoExclusive(True)
        self.dashboard_2.setObjectName("dashboard_2")
        self.verticalLayout_2.addWidget(self.dashboard_2)
        self.profile_2 = QtWidgets.QPushButton(self.icon_name_widget)
        self.profile_2.setIcon(icon1)
        self.profile_2.setCheckable(True)
        self.profile_2.setAutoExclusive(True)
        self.profile_2.setObjectName("profile_2")
        self.verticalLayout_2.addWidget(self.profile_2)
        self.messages_2 = QtWidgets.QPushButton(self.icon_name_widget)
        self.messages_2.setIcon(icon2)
        self.messages_2.setCheckable(True)
        self.messages_2.setAutoExclusive(True)
        self.messages_2.setObjectName("messages_2")
        self.verticalLayout_2.addWidget(self.messages_2)
        self.notifications_2 = QtWidgets.QPushButton(self.icon_name_widget)
        self.notifications_2.setIcon(icon3)
        self.notifications_2.setCheckable(True)
        self.notifications_2.setAutoExclusive(True)
        self.notifications_2.setObjectName("notifications_2")
        self.verticalLayout_2.addWidget(self.notifications_2)
        self.settings_2 = QtWidgets.QPushButton(self.icon_name_widget)
        self.settings_2.setIcon(icon4)
        self.settings_2.setCheckable(True)
        self.settings_2.setAutoExclusive(True)
        self.settings_2.setObjectName("settings_2")
        self.verticalLayout_2.addWidget(self.settings_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 266, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.pushButton_7 = QtWidgets.QPushButton(self.icon_name_widget)
        self.pushButton_7.setIcon(icon5)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_4.addWidget(self.pushButton_7)
        self.gridLayout.addWidget(self.icon_name_widget, 0, 1, 1, 1)
        self.main_menu = QtWidgets.QWidget(self.centralwidget)
        self.main_menu.setObjectName("main_menu")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.main_menu)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.header_widget = QtWidgets.QWidget(self.main_menu)
        self.header_widget.setObjectName("header_widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.header_widget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.menu = QtWidgets.QPushButton(self.header_widget)
        self.menu.setStyleSheet("border:none;")
        self.menu.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/menu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu.setIcon(icon6)
        self.menu.setCheckable(True)
        self.menu.setObjectName("menu")
        self.horizontalLayout.addWidget(self.menu)
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(178, 26, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.lineEdit = QtWidgets.QLineEdit(self.header_widget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_4.addWidget(self.lineEdit)
        self.pushButton_14 = QtWidgets.QPushButton(self.header_widget)
        self.pushButton_14.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_14.setIcon(icon7)
        self.pushButton_14.setObjectName("pushButton_14")
        self.horizontalLayout_4.addWidget(self.pushButton_14)
        spacerItem3 = QtWidgets.QSpacerItem(178, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.pushButton_15 = QtWidgets.QPushButton(self.header_widget)
        self.pushButton_15.setStyleSheet("border:none;")
        self.pushButton_15.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/image.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_15.setIcon(icon8)
        self.pushButton_15.setObjectName("pushButton_15")
        self.horizontalLayout_4.addWidget(self.pushButton_15)
        self.verticalLayout_5.addWidget(self.header_widget)
        self.stackedWidget = QtWidgets.QStackedWidget(self.main_menu)
        self.stackedWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.dashboard_page = QtWidgets.QWidget()
        self.dashboard_page.setObjectName("dashboard_page")
        self.label_4 = QtWidgets.QLabel(self.dashboard_page)
        self.label_4.setGeometry(QtCore.QRect(280, 150, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.stackedWidget.addWidget(self.dashboard_page)
        self.profile_page = QtWidgets.QWidget()
        self.profile_page.setObjectName("profile_page")
        self.label_5 = QtWidgets.QLabel(self.profile_page)
        self.label_5.setGeometry(QtCore.QRect(320, 170, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.stackedWidget.addWidget(self.profile_page)
        self.messages_page = QtWidgets.QWidget()
        self.messages_page.setObjectName("messages_page")
        self.label_6 = QtWidgets.QLabel(self.messages_page)
        self.label_6.setGeometry(QtCore.QRect(300, 200, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.stackedWidget.addWidget(self.messages_page)
        self.notificatiouns_pages = QtWidgets.QWidget()
        self.notificatiouns_pages.setObjectName("notificatiouns_pages")
        self.label_7 = QtWidgets.QLabel(self.notificatiouns_pages)
        self.label_7.setGeometry(QtCore.QRect(260, 210, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.stackedWidget.addWidget(self.notificatiouns_pages)
        self.settings_page = QtWidgets.QWidget()
        self.settings_page.setObjectName("settings_page")
        self.label_8 = QtWidgets.QLabel(self.settings_page)
        self.label_8.setGeometry(QtCore.QRect(300, 200, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.stackedWidget.addWidget(self.settings_page)
        self.verticalLayout_5.addWidget(self.stackedWidget)
        self.gridLayout.addWidget(self.main_menu, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.menu.toggled['bool'].connect(self.icon_only_widget.setHidden) # type: ignore
        self.menu.toggled['bool'].connect(self.icon_name_widget.setVisible) # type: ignore
        self.settings_1.toggled['bool'].connect(self.settings_2.setChecked) # type: ignore
        self.notifications_1.toggled['bool'].connect(self.notifications_2.setChecked) # type: ignore
        self.messages_1.toggled['bool'].connect(self.messages_2.setChecked) # type: ignore
        self.profile_1.toggled['bool'].connect(self.profile_2.setChecked) # type: ignore
        self.dashboard_1.toggled['bool'].connect(self.dashboard_2.setChecked) # type: ignore
        self.dashboard_2.toggled['bool'].connect(self.dashboard_1.setChecked) # type: ignore
        self.profile_2.toggled['bool'].connect(self.profile_1.setChecked) # type: ignore
        self.messages_2.toggled['bool'].connect(self.messages_1.setChecked) # type: ignore
        self.notifications_2.toggled['bool'].connect(self.notifications_1.setChecked) # type: ignore
        self.settings_2.toggled['bool'].connect(self.settings_1.setChecked) # type: ignore
        self.pushButton_6.toggled['bool'].connect(MainWindow.close) # type: ignore
        self.pushButton_7.toggled['bool'].connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "SideBar"))
        self.dashboard_2.setText(_translate("MainWindow", "Dashboard"))
        self.profile_2.setText(_translate("MainWindow", "Profile"))
        self.messages_2.setText(_translate("MainWindow", "Messages"))
        self.notifications_2.setText(_translate("MainWindow", "Notifications"))
        self.settings_2.setText(_translate("MainWindow", "Settings"))
        self.pushButton_7.setText(_translate("MainWindow", "Sign Out"))
        self.label_4.setText(_translate("MainWindow", "Dashboard Page"))
        self.label_5.setText(_translate("MainWindow", "Profile Page"))
        self.label_6.setText(_translate("MainWindow", "Messages Page"))
        self.label_7.setText(_translate("MainWindow", "Notifications Page"))
        self.label_8.setText(_translate("MainWindow", "Settings Page"))
# import resource_rc
