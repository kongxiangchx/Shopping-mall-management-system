# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui1/cus_main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_cus_main(object):
    def setupUi(self, cus_main):
        cus_main.setObjectName("cus_main")
        cus_main.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(cus_main)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(240, 110, 321, 411))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.view_goods = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.view_goods.setFont(font)
        self.view_goods.setObjectName("view_goods")
        self.verticalLayout.addWidget(self.view_goods)
        self.buy_goods = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.buy_goods.setFont(font)
        self.buy_goods.setObjectName("buy_goods")
        self.verticalLayout.addWidget(self.buy_goods)
        self.view_trade = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.view_trade.setFont(font)
        self.view_trade.setObjectName("view_trade")
        self.verticalLayout.addWidget(self.view_trade)
        self.off_trade = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.off_trade.setFont(font)
        self.off_trade.setObjectName("off_trade")
        self.verticalLayout.addWidget(self.off_trade)
        self.cus_info = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.cus_info.setFont(font)
        self.cus_info.setObjectName("cus_info")
        self.verticalLayout.addWidget(self.cus_info)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 20, 201, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        cus_main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(cus_main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        cus_main.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(cus_main)
        self.statusbar.setObjectName("statusbar")
        cus_main.setStatusBar(self.statusbar)

        self.retranslateUi(cus_main)
        QtCore.QMetaObject.connectSlotsByName(cus_main)

    def retranslateUi(self, cus_main):
        _translate = QtCore.QCoreApplication.translate
        cus_main.setWindowTitle(_translate("cus_main", "购物商城顾客端"))
        self.view_goods.setText(_translate("cus_main", "查看商品"))
        self.buy_goods.setText(_translate("cus_main", "购买商品"))
        self.view_trade.setText(_translate("cus_main", "查看交易"))
        self.off_trade.setText(_translate("cus_main", "取消交易"))
        self.cus_info.setText(_translate("cus_main", "顾客信息"))
        self.label.setText(_translate("cus_main", "购物商城顾客端"))
