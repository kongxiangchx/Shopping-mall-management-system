create database mall;
use mall;
create table shop(
shop_acc varchar(30),
shop_pass varchar(30),
shop_name varchar(30) unique,
shop_phone varchar(15),
shop_addr varchar(15),
shop_time varchar(20),
primary key(shop_acc)
);

create table goods(
shop_acc varchar(30),
goods_name varchar(30),
goods_type varchar(30),
goods_prices double check(goods_prices>=0.0),
goods_rest int check(goods_rest>=0),
goods_selled int check(goods_selled>=0),
primary key(shop_acc,goods_name),
foreign key(shop_acc) references shop(shop_acc)
);

create table customer(
cus_acc varchar(30),
cus_pass varchar(30),
cus_name varchar(30),
cus_phone varchar(15),
cus_addr varchar(30),
primary key(cus_acc)
);
create table trade(
trade_id int auto_increment,
cus_acc varchar(30),
shop_acc varchar(30),
goods_name varchar(30),
trade_num int check(trade_num>0),
trade_money double check(trade_money>=0.0),
trade_time varchar(20),
primary key(trade_id),
foreign key(cus_acc) references customer(cus_acc),
foreign key(shop_acc,goods_name) references goods(shop_acc,goods_name) on delete cascade on update cascade
);

delimiter $$
create procedure buy_goods(in cus_acc1 varchar(30),in shop_acc1 varchar(30),in goods_name1 varchar(30),in trade_num1 int,in trade_money1 double,in trade_time1 varchar(20))
begin
insert into trade(cus_acc,shop_acc,goods_name,trade_num,trade_money,trade_time) values(cus_acc1,shop_acc1,goods_name1,trade_num1,trade_money1,trade_time1);
update goods set goods_rest=goods_rest-trade_num1,goods_selled=goods_selled+trade_num1 where shop_acc=shop_acc1 and goods_name=goods_name1;
end$$
delimiter ;