create database public
CREATE TABLE items (item SERIAL PRIMARY KEY, name text not null, price numeric not null );
CREATE TABLE customers (customer SERIAL PRIMARY KEY, first_name text not null, last_name text not null);
insert in items (name, price)
value('small desk', 100), ('large desk', 300), ('fan' 80);
insert into customers(first_name, last_name)
values('Greg', 'Jones'), ('Sandra', 'Jones'), ('Scott', 'Scott'), ('Trevor', 'Green'), ('Melanie', 'Johnson')
select * from items;
select * from items where price > 80;
select * from items where price <= 300;
select * from customers where last_name = 'Smith';
--no rows returned
select * from customers where last_name ='Jones';
select * from customers where last_name != 'Scott';