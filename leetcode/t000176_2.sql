select top 1 height from users where height not in (select MAX(height) from users) order by height desc;