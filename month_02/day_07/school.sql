create database school charset = utf8;
use school

create table student
(id int primary key auto_increment,
name varchar(30),
age tinyint,
gender enum("男","女"),
hometown text
);

create table course
(id int primary key auto_increment,
course_name varchar(30),
credit tinyint,
t_id int,
constraint course_fk foreign key(t_id) references teacher(id)
on delete cascade
on update cascade
);

create table teacher
(id int primary key auto_increment,
name varchar(30),
age tinyint,
positional varchar(30)
);

create table student_course
(id int primary key auto_increment,
sid int,
cid int,
constraint student_fk foreign key(sid) references student(id)
on delete cascade
on update cascade,
constraint stu_course_fk foreign key(cid) references course(id)
on delete cascade
on update cascade
);

insert into student values
(1,'王孟何',40,'男','沧州'),
(2,'喜来乐',42,'男','沧州'),
(3,'来福',27,'男','沧州'),
(4,'赛西施',30,'女','沧州');

insert into teacher values
(1,'沈剑心','28','高级教师'),
(2,'雷利','60','海皇级'),
(3,'驴得水','10','尸位素餐');

insert into course values
(1,'高级数学','4',1),
(2,'大学英语','5',1),
(3,'空间理论','3',2),
(4,'时间理论','3',2),
(5,'物种异化论','4',3),
(6,'高级霸气','5',3);

insert into student_course values
(1,1,6),
(2,1,5),
(3,2,1),
(4,2,2),
(6,3,3),
(7,3,4),
(8,1,5);

