create table `hobby`(
    `id` int primary key auto_increment,
    `name` varchar(30) not null,
    `hobby` set('sing','dance','draw'),
    `level` char(2),
    `price` decimal(7,2),
    `remark` text
);

--插入数据
insert into class_1 values
(1,"Lily",18,'w',92),
(2,"Tom",17,'m',76);

insert into class_1 (name,age,sex,score)
values
("Abby",17,'w',87),
("Baron",19,'m',93);

insert into class_1 (name,age)
values
("Lucy",18),
("Alex",19);

insert into class_1 (age,score)
values
(18,90),
(19,88);

insert into hobby (name,hobby,level,price,remark)
values
("Joy",'sing',"A",15800,"天籁之音"),
("Lily",'sing,dance',"B",66800.888,"骨骼惊奇");

create table `hobby`(
    `id` int primary key auto_increment,
    `name` varchar(30) not null,
    `hobby` set('sing','dance','draw'),
    `level` char(2),
    `price` decimal(7,2),
    `remark` text
);

create table `books`(
    `id` int primary key auto_increment,
    `title` varchar(30) not null,
    `author` varchar(30) not null,
    `press` varchar(30) not null,
    `price` decimal(5,2) default 0,
    `remark` text
);

--插入数据
insert into books values
(1,"西游记","吴承恩",'北京大学出版社',50.50,"四大名著－中国神话"),
(2,"红楼梦","曹雪芹",'中央大学出版社',49.50,"四大名著－世家兴衰"),
(3,"水浒传","施耐庵",'南京大学出版社',51.50,"四大名著－草莽英雄"),
(4,"三国演义","罗贯中",'铁道大学出版社',49.55,"四大名著－三国争霸")；

insert into class_1 (name,age,sex,score) values ('Lucy',17,'w',81);

insert into books (`title`,`author`,`press`,`price`,`remark`) values
("Harry James Potter","J.K.罗琳","清华大学出版社",33.33,"Magical adventure");

insert into books (`title`,`author`,`press`,`price`,`remark`) values
("老人与海","海明威","清华大学出版社",36.33,"面对绝境永不言弃");

insert into books (`title`,`author`,`press`,`price`,`remark`) values
("蛙","莫言","北京大学出版社",40.33,"探索人性卑微、尴尬、纠结、矛盾的灵魂世界");

insert into books (`title`,`author`,`press`,`price`,`remark`) values
("Python编程","Mark lutz","中国电力出版社",140.33,"Python进阶必备");



insert into interest (name,hobby,level,price,remark)
values
("Joy",'sing',"A",15800,"天籁之音"),
("Lily",'sing,dance',"B",66800.888,"骨骼惊奇");