create table athlete_item
(id int primary key auto_increment,
aid int,
tid int,
constraint athlete_fk foreign key(aid) references sporter(id),
constraint item_fk foreign key(tid) references project(id)
);


alter table athlete_item add performance tinyint;