select last_name, first_name from customers where customer < 3 order by last_name;
delete from  purchases using customers where 
purchases.customer_id = customers.customer and customers.first_name = 'Scott' ;
select * from customers;
--scott still exist in the customers' table
select customers.first_name, customers.last_name, purchases.quantity_purchased from purchases 
left join customers on purchases.customer_id = customers.customer;
--it is not possible to see Scott order because Scott order has been deleted
select customers.first_name, customers.last_name, purchases.quantity_purchased from purchases 
inner join customers on purchases.customer_id = customers.customer;