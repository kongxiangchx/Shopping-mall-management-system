# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/login_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_login_window(object):
    def setupUi(self, login_window):
        login_window.setObjectName("login_window")
        login_window.resize(850, 630)
        self.centralwidget = QtWidgets.QWidget(login_window)
        self.centralwidget.setObjectName("centralwidget")
        self.toreg = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.toreg.setGeometry(QtCore.QRect(490, 280, 91, 51))
        self.toreg.setObjectName("toreg")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(190, 110, 391, 151))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.username = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.username.setFont(font)
        self.username.setObjectName("username")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.username)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.password = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.password.setFont(font)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.password)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.login_bt = QtWidgets.QPushButton(self.centralwidget)
        self.login_bt.setGeometry(QtCore.QRect(310, 390, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.login_bt.setFont(font)
        self.login_bt.setObjectName("login_bt")
        login_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(login_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 850, 26))
        self.menubar.setObjectName("menubar")
        login_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(login_window)
        self.statusbar.setObjectName("statusbar")
        login_window.setStatusBar(self.statusbar)

        self.retranslateUi(login_window)
        QtCore.QMetaObject.connectSlotsByName(login_window)

    def retranslateUi(self, login_window):
        _translate = QtCore.QCoreApplication.translate
        login_window.setWindowTitle(_translate("login_window", "购物商城顾客端"))
        self.toreg.setText(_translate("login_window", "注册"))
        self.label.setText(_translate("login_window", "用户名"))
        self.label_8.setText(_translate("login_window", "密码"))
        self.login_bt.setText(_translate("login_window", "登录"))
