select * from students;
--update students set birth_date = '02/11/1998' where last_name = 'Benichou';
--update students set last_name = 'Guez' where first_name = 'David';
--delete from students where first_name= 'Lea' and last_name= 'Benichou';
--select count(*) from students;
--alter table students add column math_grade integer;
--update students set math_grade =80 where student_id =1;
--update students set math_grade = 90 where student_id =2 or student_id = 4;
--update students set math_grade =40 where student_id = 6;
--select count(*) from students where math_grade >= 83;
--insert into students(last_name, first_name, birth_date, math_grade)
--values ('Simpson','Omer', '1980-10-03', 70);
select last_name, first_name, count(math_grade) as total_grade from students group by last_name, first_name;
select sum(math_grade) from students;

--create table purchases (id serial primary key, customer_id integer, item_id integer, foreign key (customer_id) references customers(customer), 
--foreign key (item_id) references items(item),quantity_purchased integer not null);
--select * from purchases;
--insert into purchases ( customer_id, item_id, quantity_purchased)
--values
--((select customer from customers where first_name = 'Scott' and last_name ='Scott'),
--(select item from items where name = 'fan'), 1);
--insert into purchases (customer_id, item_id, quantity_purchased)
--values
--((select customer from customers where first_name = 'Melanie' and last_name = 'Johnson'), 
--(select item from items where name = 'large desk'), 10);
--insert into purchases (customer_id, item_id, quantity_purchased)
--values
--((select customer from customers where first_name = 'Greg' and last_name = 'Jones'),
--(select item from items where name = 'small desk'), 2);

--partII
select * from purchases;
select purchases.id, purchases.customer_id, purchases.item_id, purchases.quantity_purchased,
customers.first_name, customers.last_name from purchases 
inner join customers on purchases.customer_id = customers.customer ;
select * from purchases where customer_id = 5
select * from purchases where item_id = 2 or item_id = 1 ;
select customers.first_name, customers.last_name, items.name from purchases 
join customers on purchases.customer_id = customers.customer 
join items on purchases.item_id = items.item ;


