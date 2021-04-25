import MySQLdb
import time
import datetime


class Shop_op:
    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.passwd = ''
        self.port = 3306

    def connect(self):
        self.conn = MySQLdb.connect(
            host=self.host, user=self.user, passwd=self.passwd, port=self.port, charset='utf8')
        self.conn.select_db('mall')
        self.cur = self.conn.cursor()

    def close(self):
        self.cur.close()
        self.conn.close()

    def register(self, user, passwd, shop_name, phone, addr):
        self.connect()
        self.cur.execute('select shop_acc from shop where shop_acc=%s', [user])
        data = self.cur.fetchone()
        if data is not None:
            self.close()
            return False
        value = [user, passwd, shop_name, phone, addr, time.strftime(
            '%Y-%m-%d %H:%M:%S', time.localtime(time.time()))]
        self.cur.execute('insert into shop values(%s,%s,%s,%s,%s,%s)', value)
        self.conn.commit()
        self.close()
        return True

    def login(self, user, passwd):
        self.connect()
        value = [user, passwd]
        self.cur.execute(
            'select shop_acc,shop_pass from shop where shop_acc=%s and shop_pass=%s', value)
        data = self.cur.fetchone()
        if data is not None:
            self.close()
            return True
        self.close()
        return False

    def add_goods(self, user, goods_name, goods_type, goods_prices, goods_rest):
        self.connect()
        self.cur.execute('select goods_name from goods where shop_acc=%s and goods_name=%s', [
                         user, goods_name])
        data = self.cur.fetchone()
        if data is not None:
            self.close()
            return False
        value = [user, goods_name, goods_type, goods_prices, goods_rest, 0]
        self.cur.execute('insert into goods values(%s,%s,%s,%s,%s,%s)', value)
        self.conn.commit()
        self.close()
        return True

    def view_goods(self, user, goods_name, goods_type):
        self.connect()
        if goods_type == '全部':
            self.cur.execute('select goods_name,goods_type,goods_prices,goods_rest,goods_selled from goods where shop_acc=%s and goods_name like %s', [
                             user, '%'+goods_name+'%'])
        else:
            self.cur.execute('select goods_name,goods_type,goods_prices,goods_rest,goods_selled from goods where shop_acc=%s and goods_name like %s and goods_type=%s', [
                             user, '%'+goods_name+'%', goods_type])
        data = self.cur.fetchall()
        self.close()
        return data

    def view_trade(self, user, goods_name, goods_type):
        self.connect()
        if goods_type == '全部':
            self.cur.execute('select goods.goods_name,goods_type,trade_num,trade_money,trade_time,cus_name,cus_phone,cus_addr from goods join trade join customer on goods.shop_acc=trade.shop_acc and goods.goods_name=trade.goods_name and trade.cus_acc=customer.cus_acc where goods.shop_acc=%s and goods.goods_name like %s', [
                             user, '%'+goods_name+'%'])
        else:
            self.cur.execute('select goods.goods_name,goods_type,trade_num,trade_money,trade_time,cus_name,cus_phone,cus_addr from goods join trade join customer on goods.shop_acc=trade.shop_acc and goods.goods_name=trade.goods_name and trade.cus_acc=customer.cus_acc where goods.shop_acc=%s and goods.goods_name like %s and goods_type=%s', [
                             user, '%'+goods_name+'%', goods_type])
        data = self.cur.fetchall()
        self.close()
        return data

    def select_goods(self, user):
        self.connect()
        self.cur.execute(
            'select goods_name from goods where shop_acc=%s', [user])
        data = self.cur.fetchall()
        self.close()
        return data

    def select_goodsinfo(self, user, goods_name):
        self.connect()
        self.cur.execute('select goods_name,goods_type,goods_prices,goods_rest from goods where shop_acc=%s and goods_name=%s', [
                         user, goods_name])
        data = self.cur.fetchone()
        self.close()
        return data

    def delete_goods(self, user, goods_name):
        self.connect()
        self.cur.execute('delete from goods where shop_acc=%s and goods_name=%s', [
                         user, goods_name])
        self.conn.commit()
        self.close()
        return True

    def update_goods(self, user, old_goods_name, goods_name, goods_type, goods_prices, goods_rest):
        self.connect()
        try:
            value = [goods_name, goods_type, goods_prices,
                     goods_rest, user, old_goods_name]
            self.cur.execute(
                'update goods set goods_name=%s,goods_type=%s,goods_prices=%s,goods_rest=%s where shop_acc=%s and goods_name=%s', value)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            self.close()
            return False
        self.close()
        return True

    def shop_info(self, user):
        self.connect()
        self.cur.execute(
            'select shop_acc,shop_pass,shop_name,shop_phone,shop_addr,shop_time from shop where shop_acc=%s', [user])
        data = self.cur.fetchone()
        self.close()
        return data

    def update_shop(self, user, passwd, shop_name, phone, addr):
        self.connect()
        try:
            value = [passwd, shop_name, phone, addr, user]
            self.cur.execute(
                'update shop set shop_pass=%s,shop_name=%s,shop_phone=%s,shop_addr=%s where shop_acc=%s', value)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            self.close()
            return False
        self.close()
        return True


class Customer_op:
    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.passwd = ''
        self.port = 3306

    def connect(self):
        self.conn = MySQLdb.connect(
            host=self.host, user=self.user, passwd=self.passwd, port=self.port, charset='utf8')
        self.conn.select_db('mall')
        self.cur = self.conn.cursor()

    def close(self):
        self.cur.close()
        self.conn.close()

    def register(self, user, passwd, cus_name, phone, addr):
        self.connect()
        self.cur.execute(
            'select cus_acc from customer where cus_acc=%s', [user])
        data = self.cur.fetchone()
        if data is not None:
            self.close()
            return False
        value = [user, passwd, cus_name, phone, addr]
        self.cur.execute('insert into customer values(%s,%s,%s,%s,%s)', value)
        self.conn.commit()
        self.close()
        return True

    def login(self, user, passwd):
        self.connect()
        value = [user, passwd]
        self.cur.execute(
            'select cus_acc,cus_pass from customer where cus_acc=%s and cus_pass=%s', value)
        data = self.cur.fetchone()
        if data is not None:
            self.close()
            return True
        self.close()
        return False

    def view_goods(self, goods_name, goods_type, shop_name):
        self.connect()
        if goods_type == '全部':
            self.cur.execute('select goods.goods_name,goods_type,shop_name,goods_prices,goods_rest from goods join shop on goods.shop_acc=shop.shop_acc where goods.goods_name like %s and shop_name like %s', [
                             '%'+goods_name+'%', '%'+shop_name+'%'])
        else:
            self.cur.execute('select goods.goods_name,goods_type,shop_name,goods_prices,goods_rest from goods join shop on goods.shop_acc=shop.shop_acc where goods.goods_name like %s and shop_name like %s and goods_type=%s', [
                             '%'+goods_name+'%', '%'+shop_name+'%', goods_type])
        data = self.cur.fetchall()
        self.close()
        return data

    def all_goods(self):
        self.connect()
        self.cur.execute(
            'select goods.goods_name,goods_type,shop_name,goods_prices,goods_rest,shop.shop_acc from goods join shop on goods.shop_acc=shop.shop_acc')
        data = self.cur.fetchall()
        self.close()
        return data

    def buy_goods(self, user, goods_name, shop_acc, trade_num, trade_money):
        self.connect()
        self.cur.execute('select goods_rest from goods where shop_acc=%s and goods_name=%s', [
                         shop_acc, goods_name])
        data = self.cur.fetchone()
        # print(data)
        if data is None or data[0]-int(trade_num) < 0:
            self.close()
            return False
        try:
            value = (user, shop_acc, goods_name, trade_num, trade_money, time.strftime(
                '%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
            self.cur.callproc('buy_goods', value)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            self.close()
            return False
        self.close()
        return True

    def view_trade(self, user, goods_name, goods_type):
        self.connect()
        if goods_type == '全部':
            self.cur.execute('select goods.goods_name,goods_type,shop_name,trade_num,trade_money,trade_time from shop join goods join trade join customer on shop.shop_acc=goods.shop_acc and goods.shop_acc=trade.shop_acc and goods.goods_name=trade.goods_name and trade.cus_acc=customer.cus_acc where trade.cus_acc=%s and goods.goods_name like %s', [
                             user, '%'+goods_name+'%'])
        else:
            self.cur.execute('select goods.goods_name,goods_type,shop_name,trade_num,trade_money,trade_time from shop join goods join trade join customer on shop.shop_acc=goods.shop_acc and goods.shop_acc=trade.shop_acc and goods.goods_name=trade.goods_name and trade.cus_acc=customer.cus_acc where trade.cus_acc=%s and goods.goods_name like %s and goods_type=%s', [
                             user, '%'+goods_name+'%', goods_type])
        data = self.cur.fetchall()
        self.close()
        return data

    def all_trade(self, user):
        self.connect()
        self.cur.execute(
            'select goods.goods_name,goods_type,shop_name,trade_num,trade_money,trade_time,trade.trade_id from shop join goods join trade join customer on shop.shop_acc=goods.shop_acc and goods.shop_acc=trade.shop_acc and goods.goods_name=trade.goods_name and trade.cus_acc=customer.cus_acc where trade.cus_acc=%s', [user])
        data = self.cur.fetchall()
        self.close()
        return data

    def off_trade(self, trade_id):
        self.connect()
        self.cur.execute('delete from trade where trade_id=%s', [trade_id])
        self.conn.commit()
        self.close()
        return True

    def cus_info(self, user):
        self.connect()
        self.cur.execute(
            'select cus_acc,cus_pass,cus_name,cus_phone,cus_addr from customer where cus_acc=%s', [user])
        data = self.cur.fetchone()
        self.close()
        return data

    def update_cus(self, user, passwd, cus_name, phone, addr):
        self.connect()
        try:
            value = [passwd, cus_name, phone, addr, user]
            self.cur.execute(
                'update customer set cus_pass=%s,cus_name=%s,cus_phone=%s,cus_addr=%s where cus_acc=%s', value)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            self.close()
            return False
        self.close()
        return True


if __name__ == "__main__":
    # op1=Shop_op()
    # print(op1.update_goods('haha','尿不湿升级','尿不湿升级1','母婴',30.0,20))
    # print(op1.view_goods('haha','','全部'))
    # print(op1.update_shop('haha','www','空想小店','13101661856','黑龙江省'))
    op1 = Customer_op()
    # print(op1.register('hi','www','空想','13101661856','哈理工'))
    # print(op1.login('hi','wwww'))
    # print(op1.view_goods('','数码',''))
    # print(op1.all_goods())
    # print(op1.buy_goods('hihi','尿不湿','haha','2','60'))
    # print(op1.view_goods('','全部',''))
    # print(op1.view_trade('hihi','','全部'))
    # print(op1.all_trade('hihi'))
    # print(op1.cus_info('hihi'))
