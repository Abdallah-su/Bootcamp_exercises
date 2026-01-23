alter table customer add column birth_date date;
update customer set birth_date = current_date - 
(floor(random() * (80 -18 +1)+18) * interval '1 year' 
 floor(random() * 365) * interval '1 day');
select first_name, last_name, birth_date, email from customer;