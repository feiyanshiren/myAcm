# Write your MySQL query statement below
select Email from (
select count(Email), Email from Person group by Email
    ) as t where `count(Email)` > 1