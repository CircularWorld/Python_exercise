delimiter $$
create function get_diff(id_1 int,id_2 int) returns int
begin
     declare score1 int;
     declare score2 int;
     set score1 = (select score from cls where id = id_1);
     set score2 = (select score from cls where id = id_2);
     return score1 - score2;
end $$
delimiter ;

delimiter $$
create procedure get_score(In input_name varchar(30))
begin
    declare _score int;
    set _score = (select score from cls where name = input_name);
    select _score;
end $$
delimiter ;
