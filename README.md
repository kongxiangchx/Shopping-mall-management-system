# Shopping-mall-management-system
基于Python的购物商城管理系统

## 简介
- 本项目使用Python语言编写，实现了顾客端和商家端。

## 功能
- 店主功能：注册、登录、修改店铺信息、添加商品、删除商品、修改商品、查找商品、查看交易记录。
- 顾客功能：注册、登录、修改收货信息、查找商品、购买商品、查看交易记录、取消订单。

## 商家端
- shopMain.py：编写界面上组件的功能，并通过调用send_data.py向服务器发送相应的请求。
- shop ：存放商家端的界面代码。
- ui1 ：存放商家端的ui文件，使用qtdesigner设计。
- send_data.py 将数据封装成json之后发给服务器。

## 顾客端
- customerMain.py：编写界面上组件的功能，并通过调用send_data.py向服务器发送相应的请求。
- customer ：存放顾客端的界面代码。
- ui1 ：存放顾客端的ui文件，使用qtdesigner设计。
- send_data.py 将数据封装成json之后发给服务器。

## 服务器端
- server.py：主要用来处理商家和顾客发来的请求，并调用mysql_op对数据库进行操作。
- mysql_op.py：处理商家和顾客对数据库的操作。
