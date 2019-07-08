delete from person  where Id not in (select Id from (select min(id)
 Id from person group by Email) p1);