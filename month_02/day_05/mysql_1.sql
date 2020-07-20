create table interest (
    id int primary key auto_increment,
    name varchar(30) not null,
    hobby set("sing","dance","draw"),
    level char(2),price decimal(7.2),
    remark text
);



insert into class_1 values
(5,"xiaoli",18,"s",97);

insert into class_1 (name,age,sex)
values
("Dufu",30,"m");


insert into interest (name,hobby,level,price,remark)
values
('azhen','dance,draw',"A",99999.99,"骨骼惊奇");

insert into interest (name,hobby,level,price,remark)
values
('azhen','dance',"A",999.99,'ssss');