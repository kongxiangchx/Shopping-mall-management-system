import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from customer.register_window import *
from customer.login_window import *
from customer.cus_main import *
from customer.view_goods import *
from customer.buy_goods import *
from customer.view_trade import *
from customer.off_trade import *
from customer.cus_info import *
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
        cus_name=self.cus_name.text()
        phone=self.phone.text()
        addr=self.addr.text()
        if username=='' or pass1=='' or cus_name=='' or phone=='' or addr=='':
            QMessageBox.information(self,"注册","顾客信息不能为空",QMessageBox.Yes)
            return
        if pass1!=pass2:
            QMessageBox.information(self,"注册","两次密码不同",QMessageBox.Yes)
            return
        data={'id':'customer','type':'register','user':username,'passwd':pass1,'cus_name':cus_name,'phone':phone,'addr':addr}
        #print(json.dumps(data))
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
        data={'id':'customer','type':'login','user':username,'passwd':password}
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

class Mainwin(QMainWindow, Ui_cus_main):
    def __init__(self, parent=None):
        super(Mainwin, self).__init__(parent)
        self.setupUi(self)
        self.view_goods.clicked.connect(self.click1)
        self.buy_goods.clicked.connect(self.click2)
        self.view_trade.clicked.connect(self.click3)
        self.off_trade.clicked.connect(self.click4)
        self.cus_info.clicked.connect(self.click5)
    def click1(self):
        myWin4.load()
        myWin4.show()
    def click2(self):
        myWin5.load()
        myWin5.show()
    def click3(self):
        myWin6.load()
        myWin6.show() 
    def click4(self):
        myWin7.load()
        myWin7.show()
    def click5(self):
        myWin8.load()
        myWin8.show()

class Viewgoods(QMainWindow, Ui_view_goods):
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
        shop_name=self.shop_name.text()
        data={'id':'customer','type':'view_goods','goods_name':goods_name,'goods_type':goods_type,'shop_name':shop_name}
        s=Send_data()
        recv=s.message(data)
        s.close()
        l1=len(recv['result'])
        self.model=QStandardItemModel(l1,5)
        self.model.setHorizontalHeaderLabels(['商品','类型','店铺','价格','库存'])
        for i in range(l1):
            for j in range(5):
                item=QStandardItem('%s'%(recv['result'][i][j]))
                self.model.setItem(i,j,item)
        self.goods.setModel(self.model)
    def load(self):  
        self.model=QStandardItemModel(0,5)
        self.model.setHorizontalHeaderLabels(['商品','类型','店铺','价格','库存'])
        self.goods.setModel(self.model)  
class Buygoods(QMainWindow, Ui_buy_goods):
    def __init__(self, parent=None):
        super(Buygoods, self).__init__(parent)
        self.setupUi(self)
        self.tomain.clicked.connect(self.click1)
        self.buy_bt.clicked.connect(self.click2)
        self.goods_name.currentIndexChanged.connect(self.click3)
    def click1(self):
        self.hide()
    def click2(self):
        goods_name=self.goods_name.currentText()
        if goods_name=='':
            return
        num=self.goods_name.currentIndex()
        shop_acc=self.goods_info[num][5]
        trade_num=self.buy_num.value()
        trade_money=round(trade_num*float(self.goods_price.text()),2) 
        if trade_num<=0:
            QMessageBox.information(self,"购买商品","购买数量必须大于0",QMessageBox.Yes)
            return 
        data={'id':'customer','type':'buy_goods','user':user,'goods_name':goods_name,'shop_acc':shop_acc,'trade_num':trade_num,'trade_money':trade_money}
        #print(json.dumps(data))
        s=Send_data()
        recv=s.message(data)
        s.close()
        if recv['result']=='success':
            QMessageBox.information(self,"购买商品","购买成功",QMessageBox.Yes)
        else:
            QMessageBox.information(self,"购买商品","购买失败",QMessageBox.Yes)
        self.load()
    def click3(self):
        num=self.goods_name.currentIndex()
        self.goods_type.setText(self.goods_info[num][1])
        self.goods_type.setFocusPolicy(QtCore.Qt.NoFocus)
        self.shop_name.setText(self.goods_info[num][2])
        self.shop_name.setFocusPolicy(QtCore.Qt.NoFocus)
        self.goods_price.setText(str(self.goods_info[num][3]))
        self.goods_price.setFocusPolicy(QtCore.Qt.NoFocus)
        self.goods_rest.setText(str(self.goods_info[num][4]))
        self.goods_rest.setFocusPolicy(QtCore.Qt.NoFocus)
    def load(self):
        data={'id':'customer','type':'all_goods'}
        s=Send_data()
        recv=s.message(data)
        s.close()
        self.goods_info=recv['result']
        l1=len(self.goods_info)
        self.buy_num.setValue(0)
        self.goods_name.clear()
        for i in range(l1):
            self.goods_name.addItem(self.goods_info[i][0])
        if l1>0:
            self.click3()

class Viewtrade(QMainWindow, Ui_view_trade):
    def __init__(self, parent=None):
        super(Viewtrade, self).__init__(parent)
        self.setupUi(self)
        self.tomain.clicked.connect(self.click1)
        self.ser_bt.clicked.connect(self.click2)
    def click1(self):
        self.hide()
    def click2(self):
        goods_name=self.goods_name.text()
        goods_type=self.goods_type.currentText()
        data={'id':'customer','type':'view_trade','user':user,'goods_name':goods_name,'goods_type':goods_type}
        s=Send_data()
        recv=s.message(data)
        s.close()
        #print(recv['result'])
        l1=len(recv['result'])
        self.model=QStandardItemModel(l1,6)
        self.model.setHorizontalHeaderLabels(['商品','类型','店铺','交易数量','交易金额','交易时间'])
        for i in range(l1):
            for j in range(6):
                item=QStandardItem('%s'%(recv['result'][i][j]))
                self.model.setItem(i,j,item)
        self.trade.setModel(self.model)
    def load(self):
        self.model=QStandardItemModel(0,6)
        self.model.setHorizontalHeaderLabels(['商品','类型','店铺','交易数量','交易金额','交易时间'])
        self.trade.setModel(self.model)

class Offtrade(QMainWindow, Ui_off_trade):
    def __init__(self, parent=None):
        super(Offtrade, self).__init__(parent)
        self.setupUi(self)
        self.tomain.clicked.connect(self.click1)
        self.off_bt.clicked.connect(self.click2)
        self.trade_id.currentIndexChanged.connect(self.click3)
    def click1(self):
        self.hide()
    def click2(self):
        num=self.trade_id.currentIndex()
        if num==-1:
            return 
        trade_id=self.trade_info[num][6]
        data={'id':'customer','type':'off_trade','trade_id':trade_id}
        s=Send_data()
        recv=s.message(data)
        s.close()
        if recv['result']=='success':
            QMessageBox.information(self,"取消交易","取消成功",QMessageBox.Yes)
        else:
            QMessageBox.information(self,"取消交易","取消失败",QMessageBox.Yes)
        self.load()
    def click3(self):
        num=self.trade_id.currentIndex()
        if num==-1:
            self.goods_name.clear()
            self.goods_type.clear()
            self.shop_name.clear()
            self.trade_num.clear()
            self.trade_money.clear()
            self.trade_time.clear()
            return 
        self.goods_name.setText(self.trade_info[num][0])
        self.goods_name.setFocusPolicy(QtCore.Qt.NoFocus)
        self.goods_type.setText(self.trade_info[num][1])
        self.goods_type.setFocusPolicy(QtCore.Qt.NoFocus)
        self.shop_name.setText(self.trade_info[num][2])
        self.shop_name.setFocusPolicy(QtCore.Qt.NoFocus)
        self.trade_num.setText(str(self.trade_info[num][3]))
        self.trade_num.setFocusPolicy(QtCore.Qt.NoFocus)
        self.trade_money.setText(str(self.trade_info[num][4]))
        self.trade_money.setFocusPolicy(QtCore.Qt.NoFocus)
        self.trade_time.setText(self.trade_info[num][5])
        self.trade_time.setFocusPolicy(QtCore.Qt.NoFocus)
    def load(self):
        data={'id':'customer','type':'all_trade','user':user}
        s=Send_data()
        recv=s.message(data)
        s.close()
        self.trade_info=recv['result']
        l1=len(self.trade_info)
        self.trade_id.clear()
        for i in range(l1):
            self.trade_id.addItem(str(i+1))
        if l1>0:
            self.click3()

class Cusinfo(QMainWindow, Ui_cus_info):
    def __init__(self, parent=None):
        super(Cusinfo, self).__init__(parent)
        self.setupUi(self)
        self.tomain.clicked.connect(self.click1)
        self.change_bt.clicked.connect(self.click2)
    def click1(self):
        self.hide()
    def click2(self):
        pass1=self.pass1.text()
        pass2=self.pass2.text()
        cus_name=self.cus_name.text()
        phone=self.phone.text()
        addr=self.addr.text()
        data={'id':'customer','type':'update_cus','user':user,'passwd':pass1,'cus_name':cus_name,'phone':phone,'addr':addr}
        s=Send_data()
        recv=s.message(data)
        s.close()
        if recv['result']=='success':
            QMessageBox.information(self,"修改顾客信息","修改成功",QMessageBox.Yes)
        else:
            QMessageBox.information(self,"修改顾客信息","修改失败",QMessageBox.Yes)
        self.load()
    def load(self):
        data={'id':'customer','type':'cus_info','user':user}
        s=Send_data()
        recv=s.message(data)
        s.close()
        self.username.setText(recv['result'][0])
        self.username.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pass1.setText(recv['result'][1])
        self.pass2.setText(recv['result'][1])
        self.cus_name.setText(recv['result'][2])
        self.phone.setText(recv['result'][3])
        self.addr.setText(recv['result'][4])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    user=""
    myWin1=Register()
    myWin1.show()
    myWin2=Login()
    myWin3=Mainwin()
    myWin4=Viewgoods()
    #myWin4.show()
    myWin5=Buygoods()
    myWin6=Viewtrade()
    myWin7=Offtrade()
    myWin8=Cusinfo()
    if app.exec_()==0:
        sys.exit(0)