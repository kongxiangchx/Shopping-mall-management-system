# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/shop_info.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_shop_info(object):
    def setupUi(self, shop_info):
        shop_info.setObjectName("shop_info")
        shop_info.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(shop_info)
        self.centralwidget.setObjectName("centralwidget")
        self.change_bt = QtWidgets.QPushButton(self.centralwidget)
        self.change_bt.setGeometry(QtCore.QRect(320, 410, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.change_bt.setFont(font)
        self.change_bt.setObjectName("change_bt")
        self.tomain = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.tomain.setGeometry(QtCore.QRect(510, 330, 91, 51))
        self.tomain.setObjectName("tomain")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(210, 30, 391, 287))
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
        self.pass1 = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pass1.setFont(font)
        self.pass1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass1.setObjectName("pass1")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pass1)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.shop_name = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.shop_name.setFont(font)
        self.shop_name.setObjectName("shop_name")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.shop_name)
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.phone = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.phone.setFont(font)
        self.phone.setObjectName("phone")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.phone)
        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.addr = QtWidgets.QComboBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.addr.setFont(font)
        self.addr.setObjectName("addr")
        self.addr.addItem("")
        self.addr.addItem("")
        self.addr.addItem("")
        self.addr.addItem("")
        self.addr.addItem("")
        self.addr.addItem("")
        self.addr.addItem("")
        self.addr.addItem("")
        self.addr.addItem("")
        self.addr.addItem("")
        self.addr.addItem("")
        self.addr.addItem("")
        self.addr.addItem("")
        self.addr.addItem("")
        self.addr.addItem("")
        self.addr.addItem("")
        self.addr.addItem("")
        self.addr.addItem("")
        self.addr.addItem("")
        self.addr.addItem("")
        self.addr.addItem("")
        self.addr.addItem("")
        self.addr.addItem("")
        self.addr.addItem("")
        self.addr.addItem("")
        self.addr.addItem("")
        self.addr.addItem("")
        self.addr.addItem("")
        self.addr.addItem("")
        self.addr.addItem("")
        self.addr.addItem("")
        self.addr.addItem("")
        self.addr.addItem("")
        self.addr.addItem("")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.addr)
        self.pass2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pass2.setFont(font)
        self.pass2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass2.setObjectName("pass2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.pass2)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.label_12 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.shop_time = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.shop_time.setFont(font)
        self.shop_time.setObjectName("shop_time")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.shop_time)
        shop_info.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(shop_info)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        shop_info.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(shop_info)
        self.statusbar.setObjectName("statusbar")
        shop_info.setStatusBar(self.statusbar)

        self.retranslateUi(shop_info)
        QtCore.QMetaObject.connectSlotsByName(shop_info)

    def retranslateUi(self, shop_info):
        _translate = QtCore.QCoreApplication.translate
        shop_info.setWindowTitle(_translate("shop_info", "????????????"))
        self.change_bt.setText(_translate("shop_info", "??????????????????"))
        self.tomain.setText(_translate("shop_info", "??????"))
        self.label.setText(_translate("shop_info", "?????????"))
        self.label_9.setText(_translate("shop_info", "?????????"))
        self.label_10.setText(_translate("shop_info", "????????????"))
        self.label_11.setText(_translate("shop_info", "?????????"))
        self.addr.setItemText(0, _translate("shop_info", "?????????"))
        self.addr.setItemText(1, _translate("shop_info", "?????????"))
        self.addr.setItemText(2, _translate("shop_info", "?????????"))
        self.addr.setItemText(3, _translate("shop_info", "?????????"))
        self.addr.setItemText(4, _translate("shop_info", "?????????"))
        self.addr.setItemText(5, _translate("shop_info", "?????????"))
        self.addr.setItemText(6, _translate("shop_info", "?????????"))
        self.addr.setItemText(7, _translate("shop_info", "?????????"))
        self.addr.setItemText(8, _translate("shop_info", "????????????"))
        self.addr.setItemText(9, _translate("shop_info", "?????????"))
        self.addr.setItemText(10, _translate("shop_info", "?????????"))
        self.addr.setItemText(11, _translate("shop_info", "?????????"))
        self.addr.setItemText(12, _translate("shop_info", "?????????"))
        self.addr.setItemText(13, _translate("shop_info", "?????????"))
        self.addr.setItemText(14, _translate("shop_info", "?????????"))
        self.addr.setItemText(15, _translate("shop_info", "?????????"))
        self.addr.setItemText(16, _translate("shop_info", "?????????"))
        self.addr.setItemText(17, _translate("shop_info", "?????????"))
        self.addr.setItemText(18, _translate("shop_info", "?????????"))
        self.addr.setItemText(19, _translate("shop_info", "?????????"))
        self.addr.setItemText(20, _translate("shop_info", "?????????"))
        self.addr.setItemText(21, _translate("shop_info", "?????????"))
        self.addr.setItemText(22, _translate("shop_info", "?????????"))
        self.addr.setItemText(23, _translate("shop_info", "?????????"))
        self.addr.setItemText(24, _translate("shop_info", "?????????"))
        self.addr.setItemText(25, _translate("shop_info", "?????????"))
        self.addr.setItemText(26, _translate("shop_info", "?????????"))
        self.addr.setItemText(27, _translate("shop_info", "??????????????????"))
        self.addr.setItemText(28, _translate("shop_info", "?????????????????????"))
        self.addr.setItemText(29, _translate("shop_info", "???????????????"))
        self.addr.setItemText(30, _translate("shop_info", "?????????????????????"))
        self.addr.setItemText(31, _translate("shop_info", "????????????????????????"))
        self.addr.setItemText(32, _translate("shop_info", "?????????????????????"))
        self.addr.setItemText(33, _translate("shop_info", "?????????????????????"))
        self.label_8.setText(_translate("shop_info", "????????????"))
        self.label_7.setText(_translate("shop_info", "??????"))
        self.label_12.setText(_translate("shop_info", "????????????"))
