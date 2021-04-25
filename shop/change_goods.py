# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/change_goods.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_change_goods(object):
    def setupUi(self, change_goods):
        change_goods.setObjectName("change_goods")
        change_goods.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(change_goods)
        self.centralwidget.setObjectName("centralwidget")
        self.toupdate = QtWidgets.QPushButton(self.centralwidget)
        self.toupdate.setGeometry(QtCore.QRect(220, 310, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.toupdate.setFont(font)
        self.toupdate.setObjectName("toupdate")
        self.delete_bt = QtWidgets.QPushButton(self.centralwidget)
        self.delete_bt.setGeometry(QtCore.QRect(450, 310, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.delete_bt.setFont(font)
        self.delete_bt.setObjectName("delete_bt")
        self.tomain = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.tomain.setGeometry(QtCore.QRect(520, 180, 91, 51))
        self.tomain.setObjectName("tomain")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(220, 130, 391, 41))
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
        self.goods_name = QtWidgets.QComboBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.goods_name.setFont(font)
        self.goods_name.setObjectName("goods_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.goods_name)
        change_goods.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(change_goods)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        change_goods.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(change_goods)
        self.statusbar.setObjectName("statusbar")
        change_goods.setStatusBar(self.statusbar)

        self.retranslateUi(change_goods)
        QtCore.QMetaObject.connectSlotsByName(change_goods)

    def retranslateUi(self, change_goods):
        _translate = QtCore.QCoreApplication.translate
        change_goods.setWindowTitle(_translate("change_goods", "修改商品"))
        self.toupdate.setText(_translate("change_goods", "修改商品"))
        self.delete_bt.setText(_translate("change_goods", "删除商品"))
        self.tomain.setText(_translate("change_goods", "首页"))
        self.label.setText(_translate("change_goods", "商品名称"))
