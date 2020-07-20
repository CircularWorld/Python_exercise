1.连接数据库
mysql -u root -p

2.创建数据库
create database tools character set utf8;

3.切换库
use tools;

4.查看库
select database();

5.删除库
drop database tools;

6.创建表
create table tool(id tinyint primary key auto_increment,name varchar(10) not null,effect text);

7.插入数据
insert into tool values(1,'查询','查找单词');

8.查询
select*from tool;
select name,effect from tool;



----------------
--alter语句
alter table interest add tel char(11) after price;
--删除字段
alter table interest drop tel;
--修改字段类型
alter table interest modify tel char(16);
--修改字段名
alter table interest change tel phone　char(16);
--修改表名
alter table interest rename hobby;

--books 修改
update  book set price = 45 where title = '呐喊';

alter table book add publish data after price;


select * from sanguo where country ='蜀'and attack > (select attack from sanguo where country = '魏' order by attack desc limit 1);


select * from sanguo where gender = '女' union select * from sanguo where gender ='男'and attack <250;