import threading
import time
import queue
import socket
import json
from mysql_op import *


class Shop:
    def __init__(self, conn):
        self.conn = conn

    def register(self, recv):
        op1 = Shop_op()
        if op1.register(recv['user'], recv['passwd'], recv['shop_name'], recv['phone'], recv['addr']):
            data = {'result': 'success'}
        else:
            data = {'result': 'fail'}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()

    def login(self, recv):
        op1 = Shop_op()
        if op1.login(recv['user'], recv['passwd']):
            data = {'result': 'success'}
        else:
            data = {'result': 'fail'}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()

    def addgoods(self, recv):
        op1 = Shop_op()
        if op1.add_goods(recv['user'], recv['goods_name'], recv['goods_type'], recv['goods_prices'], recv['goods_rest']):
            data = {'result': 'success'}
        else:
            data = {'result': 'fail'}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()

    def viewgoods(self, recv):
        op1 = Shop_op()
        data = {'result': op1.view_goods(
            recv['user'], recv['goods_name'], recv['goods_type'])}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()

    def viewtrade(self, recv):
        op1 = Shop_op()
        data = {'result': op1.view_trade(
            recv['user'], recv['goods_name'], recv['goods_type'])}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()

    def selectgoods(self, recv):
        op1 = Shop_op()
        data = {'result': op1.select_goods(recv['user'])}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()

    def deletegoods(self, recv):
        op1 = Shop_op()
        if op1.delete_goods(recv['user'], recv['goods_name']):
            data = {'result': 'success'}
        else:
            data = {'result': 'fail'}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()

    def selectgoodsinfo(self, recv):
        op1 = Shop_op()
        # data={'result':'success'}
        data = {'result': op1.select_goodsinfo(
            recv['user'], recv['goods_name'])}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()

    def updategoods(self, recv):
        op1 = Shop_op()
        if op1.update_goods(recv['user'], recv['old_goods_name'], recv['goods_name'], recv['goods_type'], recv['goods_prices'], recv['goods_rest']):
            data = {'result': 'success'}
        else:
            data = {'result': 'fail'}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()

    def shopinfo(self, recv):
        op1 = Shop_op()
        data = {'result': op1.shop_info(recv['user'])}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()

    def updateshop(self, recv):
        op1 = Shop_op()
        if op1.update_shop(recv['user'], recv['passwd'], recv['shop_name'], recv['phone'], recv['addr']):
            data = {'result': 'success'}
        else:
            data = {'result': 'fail'}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()


class Customer:
    def __init__(self, conn):
        self.conn = conn

    def register(self, recv):
        op1 = Customer_op()
        if op1.register(recv['user'], recv['passwd'], recv['cus_name'], recv['phone'], recv['addr']):
            data = {'result': 'success'}
        else:
            data = {'result': 'fail'}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()

    def login(self, recv):
        op1 = Customer_op()
        if op1.login(recv['user'], recv['passwd']):
            data = {'result': 'success'}
        else:
            data = {'result': 'fail'}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()

    def viewgoods(self, recv):
        op1 = Customer_op()
        data = {'result': op1.view_goods(
            recv['goods_name'], recv['goods_type'], recv['shop_name'])}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()

    def allgoods(self, recv):
        op1 = Customer_op()
        data = {'result': op1.all_goods()}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()

    def buygoods(self, recv):
        op1 = Customer_op()
        if op1.buy_goods(recv['user'], recv['goods_name'], recv['shop_acc'], recv['trade_num'], recv['trade_money']):
            data = {'result': 'success'}
        else:
            data = {'result': 'fail'}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()

    def viewtrade(self, recv):
        op1 = Customer_op()
        data = {'result': op1.view_trade(
            recv['user'], recv['goods_name'], recv['goods_type'])}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()

    def alltrade(self, recv):
        op1 = Customer_op()
        data = {'result': op1.all_trade(recv['user'])}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()

    def offtrade(self, recv):
        op1 = Customer_op()
        if op1.off_trade(recv['trade_id']):
            data = {'result': 'success'}
        else:
            data = {'result': 'fail'}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()

    def cusinfo(self, recv):
        op1 = Customer_op()
        data = {'result': op1.cus_info(recv['user'])}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()

    def updatecus(self, recv):
        op1 = Customer_op()
        if op1.update_cus(recv['user'], recv['passwd'], recv['cus_name'], recv['phone'], recv['addr']):
            data = {'result': 'success'}
        else:
            data = {'result': 'fail'}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()


if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 5000))
    s.listen(20)
    while True:
        conn, addr = s.accept()
        recv = json.loads(conn.recv(1024).decode())
        print(json.dumps(recv))
        if recv['id'] == 'shop':
            Shop1 = Shop(conn)
            if recv['type'] == 'register':
                Shop1.register(recv)
            elif recv['type'] == 'login':
                Shop1.login(recv)
            elif recv['type'] == 'add_goods':
                Shop1.addgoods(recv)
            elif recv['type'] == 'view_goods':
                Shop1.viewgoods(recv)
            elif recv['type'] == 'view_trade':
                Shop1.viewtrade(recv)
            elif recv['type'] == 'select_goods':
                Shop1.selectgoods(recv)
            elif recv['type'] == 'delete_goods':
                Shop1.deletegoods(recv)
            elif recv['type'] == 'select_goodsinfo':
                Shop1.selectgoodsinfo(recv)
            elif recv['type'] == 'update_goods':
                Shop1.updategoods(recv)
            elif recv['type'] == 'shop_info':
                Shop1.shopinfo(recv)
            elif recv['type'] == 'update_shop':
                Shop1.updateshop(recv)
        else:
            Cus1 = Customer(conn)
            if recv['type'] == 'register':
                Cus1.register(recv)
            elif recv['type'] == 'login':
                Cus1.login(recv)
            elif recv['type'] == 'view_goods':
                Cus1.viewgoods(recv)
            elif recv['type'] == 'all_goods':
                Cus1.allgoods(recv)
            elif recv['type'] == 'buy_goods':
                Cus1.buygoods(recv)
            elif recv['type'] == 'view_trade':
                Cus1.viewtrade(recv)
            elif recv['type'] == 'all_trade':
                Cus1.alltrade(recv)
            elif recv['type'] == 'off_trade':
                Cus1.offtrade(recv)
            elif recv['type'] == 'cus_info':
                Cus1.cusinfo(recv)
            elif recv['type'] == 'update_cus':
                Cus1.updatecus(recv)
