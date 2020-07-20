create database books charset = utf8;

use books;

create table book(
id int primary key auto_increment,
title varchar(50) not null,
author varchar(30) not null,
publication varchar(30) not null,
price DECIMAL(5,2) default 0,
remark text
);

insert into book
(title,author,publication,price,remark)
values
("边城","沈从文","机械工业出版社",88,"小城故事多"),
("骆驼祥子","老舍","机械工业出版社",45,"你是祥子吗"),
("呐喊","鲁迅","人民教育出版社",47,"最后的声音"),
("朝花夕拾","鲁迅","人民教育出版社",88,"好时光"),
("围城","钱钟书","中国文学出版社",53,"你心中的围城"),
("茶馆","老舍","人民教育出版社",70,"茶馆故事"),
("老人与海","海明威","人民教育出版社",80,"海上搏斗"),
("哈利波特","J.K","人民教育出版社",77,"魔法冒险");



