select p.Email from Person p left join (select Id,Email from Person group by Email) a on p.id = a.id where a.id is null group by p.Email