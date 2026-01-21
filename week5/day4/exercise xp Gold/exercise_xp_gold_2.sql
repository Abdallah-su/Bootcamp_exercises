select rating, count(title) from film group by rating;

--Get a list of all the movies that have a rating of G or PG-13.
--Filter this list further: look for only movies that are under 2 hours long,
--and whose rental price (rental_rate) is under 3.00. 
--Sort the list alphabetically.
select title from film where rating = 'G' OR rating = 'PG-13' and
length < 120  and rental_rate < 3 order by title;



--Find a customer in the customer table, and change his/her details to your 
--details, using SQL UPDATE.
--Now find the customer’s address, and use UPDATE to change the address 
--to your address (or make one up).
update customer set first_name  = 'Adwoa', last_name = 'Mansa' 
where customer_id = 4;
select * from customer;
