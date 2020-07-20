---books
---book
    --- b_id title publish_time price au_id pub_id
---author
    ---a_id name
---publish
    ---p_id pub_name
create database pubook character set utf8;
use pubook;
create table book(
b_id int primary key auto_increment,
title varchar(40),
publish_time date,
price decimal(5,2),
au_id int,
pub_id int,
foreign key(au_id) references author(a_id),
foreign key(pub_id) references publish(p_id)
);

create table author(
a_id int primary key auto_increment,
name varchar(30)
);

create table publish(
p_id int primary key auto_increment,
pub_name varchar(40)
);
