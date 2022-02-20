# Shopping-mall-management-system
基于Python的购物商城管理系统

## 简介
- 本项目使用Python语言编写，实现了顾客端和商家端。

## 功能
- 商家功能：注册、登录、修改店铺信息、添加商品、删除商品、修改商品、查找商品、查看交易记录。
- 顾客功能：注册、登录、修改收货信息、查找商品、购买商品、查看交易记录、取消订单。

## 商家端
- shopMain.py：编写界面上组件的功能，并通过调用send_data.py向服务器发送相应的请求。
- shop ：存放商家端的界面代码。
- ui2 ：存放商家端的ui文件，使用qtdesigner设计。
- send_data.py 将数据封装成json之后发给服务器。

## 顾客端
- customerMain.py：编写界面上组件的功能，并通过调用send_data.py向服务器发送相应的请求。
- customer ：存放顾客端的界面代码。
- ui1 ：存放顾客端的ui文件，使用qtdesigner设计。
- send_data.py 将数据封装成json之后发给服务器。

## 服务器端
- server.py：主要用来处理商家和顾客发来的请求，并调用mysql_op对数据库进行操作。
- mysql_op.py：处理商家和顾客对数据库的操作。

## 项目运行

1. 通过mall.sql文件创建数据库、相关数据表和触发器。
2. 运行server.py文件，即开启服务器。
3. 若是商家，就运行shopMain.py文件；若是顾客，就运行customerMain.py文件。

## 界面展示

### 商家端

- 商家注册

<img src="pic\图片1.jpg" alt="图片1" style="zoom:25%;" />

- 商家登录

<img src="pic\图片2.jpg" alt="图片2" style="zoom:25%;" />

- 商家端主界面

<img src="pic\图片3.jpg" alt="图片3" style="zoom:25%;" />

- 添加商品

<img src="pic\图片4.jpg" alt="图片4" style="zoom:25%;" />

- 查看商品

<img src="pic\图片5.jpg" alt="图片5" style="zoom:25%;" />

- 修改商品

<img src="pic\图片6.jpg" alt="图片6" style="zoom:25%;" />

<img src="pic\图片7.jpg" alt="图片7" style="zoom:25%;" />

- 查看交易

<img src="pic\图片8.jpg" alt="图片8" style="zoom:25%;" />

- 店铺信息

<img src="pic\图片9.jpg" alt="图片9" style="zoom:25%;" />

### 顾客端

- 顾客注册

<img src="pic\图片10.jpg" alt="图片10" style="zoom:25%;" />

- 顾客登录

<img src="pic\图片11.jpg" alt="图片11" style="zoom:25%;" />

- 顾客端主界面

<img src="pic\图片12.jpg" alt="图片12" style="zoom:25%;" />

- 查看商品

<img src="pic\图片13.jpg" alt="图片13" style="zoom:25%;" />

- 购买商品

<img src="pic\图片14.jpg" alt="图片14" style="zoom:25%;" />

- 查看交易

<img src="pic\图片15.jpg" alt="图片15" style="zoom:25%;" />

- 取消交易

<img src="pic\图片16.jpg" alt="图片16" style="zoom:25%;" />

- 顾客信息

<img src="pic\图片17.jpg" alt="图片17" style="zoom:25%;" />
