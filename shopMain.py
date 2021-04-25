import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import shop.register_window
from shop.register_window import *
from shop.login_window import *
from shop.shop_main import *
from shop.add_goods import *
from shop.view_goods import *
from shop.change_goods import *
from shop.update_goods import *
from shop.view_trade import *
from shop.shop_info import *
from send_data import *

class Register(QMainWindow, Ui_register_window):
    def __init__(self, parent=None):
        super(Register, self).__init__(parent)
        self.setupUi(self)
        self.reg_bt.clicked.connect(self.click1)
        self.tologin.clicked.connect(self.click2)
    def click1(self):
        username=self.username.text()
        pass1=self.pass1.text()
        pass2=self.pass2.text()
        shop_name=self.shop_name.text()
        phone=self.phone.text()
        addr=self.addr.currentText()
        if username=='' or pass1=='' or shop_name=='' or phone=='' or addr=='':
            QMessageBox.information(self,"注册","店铺信息不能为空",QMessageBox.Yes)
            return
        if pass1!=pass2:
            QMessageBox.information(self,"注册","两次密码不同",QMessageBox.Yes)
            return
        data={'id':'shop','type':'register','user':username,'passwd':pass1,'shop_name':shop_name,'phone':phone,'addr':addr}
        s=Send_data()
        recv=s.message(data)
        s.close()
        if recv['result']=='success':
            QMessageBox.information(self,"注册","注册成功",QMessageBox.Yes)
        else:
            QMessageBox.information(self,"注册","注册失败",QMessageBox.Yes)
    def click2(self):
        myWin1.hide()
        myWin2.show()
        
class Login(QMainWindow, Ui_login_window):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.setupUi(self)
        self.login_bt.clicked.connect(self.click1)
        self.toreg.clicked.connect(self.click2)
    def click1(self):
        global user
        username=self.username.text()
        password=self.password.text()
        if username=='' or password=='':
            QMessageBox.information(self,"登录","用户名和密码不能为空",QMessageBox.Yes)
            return
        data={'id':'shop','type':'login','user':username,'passwd':password}
        s=Send_data()
        recv=s.message(data)
        s.close()
        if recv['result']=='success':
            QMessageBox.information(self,"登录","登录成功",QMessageBox.Yes)
            user=username
            myWin2.hide()
            myWin3.show()
        else:
            QMessageBox.information(self,"登录","登录失败",QMessageBox.Yes)
    def click2(self):
        myWin2.hide()
        myWin1.show() 

class Mainwin(QMainWindow, Ui_shop_main):
    def __init__(self, parent=None):
        super(Mainwin, self).__init__(parent)
        self.setupUi(self)
        self.add_goods.clicked.connect(self.click1)
        self.view_goods.clicked.connect(self.click2)
        self.change_goods.clicked.connect(self.click3)
        self.view_trade.clicked.connect(self.click4)
        self.shop_info.clicked.connect(self.click5)
    def click1(self):
        myWin4.show()
    def click2(self):
        myWin5.load()
        myWin5.show()
    def click3(self):
        myWin6.load()
        myWin6.show()
    def click4(self):
        myWin7.show()
    def click5(self):
        myWin8.load()
        myWin8.show()

class Addgoods(QMainWindow, Ui_add_goods):
    global user
    def __init__(self, parent=None):
        super(Addgoods, self).__init__(parent)
        self.setupUi(self)
        self.tomain.clicked.connect(self.click1)
        self.add_bt.clicked.connect(self.click2)
    def click1(self):
        self.hide()
    def click2(self):
        goods_name=self.goods_name.text()
        goods_type=self.goods_type.currentText()
        goods_prices=float(self.goods_prices.text())
        goods_rest=int(self.goods_rest.text())
        data={'id':'shop','user':user,'type':'add_goods','goods_name':goods_name,'goods_type':goods_type,'goods_prices':goods_prices,'goods_rest':goods_rest}
        s=Send_data()
        recv=s.message(data)
        if recv['result']=='success':
            QMessageBox.information(self,"添加商品","添加成功",QMessageBox.Yes)
        else:
            QMessageBox.information(self,"添加商品","添加失败",QMessageBox.Yes)
        s.close()
class Viewgoods(QMainWindow, Ui_view_goods):
    global user
    def __init__(self, parent=None):
        super(Viewgoods, self).__init__(parent)
        self.setupUi(self)
        self.tomain.clicked.connect(self.click1)
        self.ser_bt.clicked.connect(self.click2)
    def click1(self):
        self.hide()
    def click2(self):
        goods_name=self.goods_name.text()
        goods_type=self.goods_type.currentText()
        data={'id':'shop','type':'view_goods','user':user,'goods_name':goods_name,'goods_type':goods_type}
        s=Send_data()
        recv=s.message(data)
        s.close()
        l1=len(recv['result'])
        self.model=QStandardItemModel(l1,5)
        self.model.setHorizontalHeaderLabels(['名称','类型','价格','库存','已售'])
        for i in range(l1):
            for j in range(5):
                item=QStandardItem('%s'%(recv['result'][i][j]))
                self.model.setItem(i,j,item)
        self.goods.setModel(self.model)
    def load(self):  
        self.model=QStandardItemModel(0,5)
        self.model.setHorizontalHeaderLabels(['名称','类型','价格','库存','已售'])
        self.goods.setModel(self.model)  
class Changegoods(QMainWindow, Ui_change_goods):
    def __init__(self,parent=None):
        super(Changegoods,self).__init__(parent)
        self.setupUi(self)
        self.tomain.clicked.connect(self.click1)
        self.delete_bt.clicked.connect(self.click2)
        self.toupdate.clicked.connect(self.click3)
    def click1(self):
        self.hide()
    def click2(self):
        goods_name=self.goods_name.currentText()
        if goods_name=='':
            return 
        data={'id':'shop','type':'delete_goods','user':user,'goods_name':goods_name}
        #print(json.dumps(data))
        s=Send_data()
        recv=s.message(data)
        s.close()
        if recv['result']=='success':
            self.load()
            QMessageBox.information(self,"删除商品","删除成功",QMessageBox.Yes)
        else:
            QMessageBox.information(self,"删除商品","删除失败",QMessageBox.Yes)
    def click3(self):
        goods_name=self.goods_name.currentText()
        #print(goods_name)
        if goods_name!='':
            myWin9.load(goods_name)
            myWin9.show()
    def load(self):
        data={'id':'shop','type':'select_goods','user':user}
        s=Send_data()
        recv=s.message(data)
        s.close()
        #print(recv['result'])
        l1=len(recv['result'])
        self.goods_name.clear()
        for i in range(l1):
            self.goods_name.addItem(recv['result'][i][0])

class Updategoods(QMainWindow,Ui_update_goods):
    def __init__(self,parent=None):
        super(Updategoods,self).__init__(parent)
        self.setupUi(self)
        self.tofront.clicked.connect(self.click1)
        self.update_bt.clicked.connect(self.click2)
    def click1(self):
        self.hide()
    def click2(self):
        old_goods_name=self.old_goods_name
        goods_name=self.goods_name.text()
        goods_type=self.goods_type.currentText()
        goods_prices=float(self.goods_prices.text())
        goods_rest=int(self.goods_rest.text())
        data={'id':'shop','type':'update_goods','user':user,'old_goods_name':old_goods_name,'goods_name':goods_name,'goods_type':goods_type,'goods_prices':goods_prices,'goods_rest':goods_rest}
        s=Send_data()
        recv=s.message(data)
        s.close()
        if recv['result']=='success':
            self.hide()
            myWin6.load()
            QMessageBox.information(self,"修改商品","修改成功",QMessageBox.Yes)
        else:
            QMessageBox.information(self,"修改商品","修改失败",QMessageBox.Yes)
    def load(self,goods_name):
        self.old_goods_name=goods_name
        data={'id':'shop','type':'select_goodsinfo','user':user,'goods_name':goods_name}
        #print(json.dumps(data))
        s=Send_data()
        recv=s.message(data)
        s.close()
        #print(recv['result'])
        self.goods_name.setText(recv['result'][0])
        self.goods_type.setCurrentText(recv['result'][1])
        self.goods_prices.setValue(recv['result'][2])
        self.goods_rest.setValue(recv['result'][3])

class Viewtrade(QMainWindow,Ui_view_trade):
    def __init__(self,parent=None):
        super(Viewtrade,self).__init__(parent)
        self.setupUi(self)
        self.tomain.clicked.connect(self.click1)
        self.ser_bt.clicked.connect(self.click2)
    def click1(self):
        self.hide()
    def click2(self):
        goods_name=self.goods_name.text()
        goods_type=self.goods_type.currentText()
        data={'id':'shop','type':'view_trade','user':user,'goods_name':goods_name,'goods_type':goods_type}
        s=Send_data()
        recv=s.message(data)
        s.close()
        #print(recv['result'])
        l1=len(recv['result'])
        self.model=QStandardItemModel(l1,8)
        self.model.setHorizontalHeaderLabels(['商品名称','商品类型','交易数量','交易金额','交易时间','顾客','联系方式','收货地址'])
        for i in range(l1):
            for j in range(8):
                item=QStandardItem('%s'%(recv['result'][i][j]))
                self.model.setItem(i,j,item)
        self.trade.setModel(self.model)
    def load(self):
        self.model=QStandardItemModel(0,8)
        self.model.setHorizontalHeaderLabels(['商品名称','商品类型','交易数量','交易金额','交易时间','顾客','联系方式','收货地址'])
        self.trade.setModel(self.model)
class Shopinfo(QMainWindow, Ui_shop_info):
    def __init__(self, parent=None):
        super(Shopinfo, self).__init__(parent)
        self.setupUi(self)
        self.tomain.clicked.connect(self.click1)
        self.change_bt.clicked.connect(self.click2)
    def click1(self):
        self.hide()
    def click2(self):
        pass1=self.pass1.text()
        pass2=self.pass2.text()
        shop_name=self.shop_name.text()
        phone=self.phone.text()
        addr=self.addr.currentText()
        data={'id':'shop','type':'update_shop','user':user,'passwd':pass1,'shop_name':shop_name,'phone':phone,'addr':addr}
        s=Send_data()
        recv=s.message(data)
        s.close()
        if recv['result']=='success':
            QMessageBox.information(self,"修改店铺信息","修改成功",QMessageBox.Yes)
        else:
            QMessageBox.information(self,"修改店铺信息","修改失败",QMessageBox.Yes)
        self.load()
    def load(self):
        data={'id':'shop','type':'shop_info','user':user}
        s=Send_data()
        recv=s.message(data)
        s.close()
        self.username.setText(recv['result'][0])
        self.username.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pass1.setText(recv['result'][1])
        self.pass2.setText(recv['result'][1])
        self.shop_name.setText(recv['result'][2])
        self.phone.setText(recv['result'][3])
        self.addr.setCurrentText(recv['result'][4])
        self.shop_time.setText(recv['result'][5])
        self.shop_time.setFocusPolicy(QtCore.Qt.NoFocus)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    user=""
    myWin1=Register()
    myWin1.show()
    myWin2=Login()
    myWin3=Mainwin()
    myWin4=Addgoods()
    #myWin4.show()
    myWin5=Viewgoods()
    #myWin5.show()
    myWin6=Changegoods()
    #myWin6.show()
    myWin7=Viewtrade()
    #myWin7.show()
    myWin8=Shopinfo()
    #myWin8.show()
    myWin9=Updategoods()
    if app.exec_()==0:
        sys.exit(0)