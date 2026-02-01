CREATE DATABASE shop;
CREATE TABLE items (item SERIAL PRIMARY KEY, name text not null, price numeric not null );
CREATE TABLE customers (customer SERIAL PRIMARY KEY, first_name text not null, last_name text not null);
INSERT INTO items (name, price)
VALUES ('small desk', 100), ('large desk', 300), ('fan', 80);
INSERT INTO customers(first_name, last_name)
VALUES('Greg', 'Jones'), ('Sandra', 'Jones'), ('Scott', 'Scott'), ('Trevor', 'Green'), ('Melanie', 'Johnson');
SELECT * FROM items;
SELECT * FROM items where price > 80;
SELECT * FROM items where price <= 300;
SELECT * FROM customers where last_name = 'Smith';
--no rows returned
SELECT * FROM customers where last_name ='Jones';
SELECT * FROM customers where first_name != 'Scott';