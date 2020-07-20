---朋友圈 wechat
---用户：
    ---id account,pwd,tel
---朋友圈 moments
    ---id picture info place time user_id
---点赞 评论
    ---id  like comment user_id moments_id

create database wechat character set utf8;

use wechat;

create table user(
id int primary key auto_increment,
account varchar(30) not null,
password varchar(30) not null,
mobile_number int
);

create table pyq(
id int primary key auto_increment,
image blob,
content text,
time datetime,
user_id int,
foreign key(user_id) references user(id)
);

create table user_pyq(
id int primary key auto_increment,
`like` bit,
comment text default null,
u_id int,
p_id int,
foreign key(u_id) references user(id),
foreign key(p_id) references pyq(id)
);