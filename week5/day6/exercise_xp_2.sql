UPDATE film SET language_id =2 WHERE film_id IN (1,4,6,8);
SELECT * FROM film;
-- customer_address_id, this is linked to the address table, thus a new address_id can not be created in the customer table if it's not founf in the address table.
DROP TABLE customer_review;
SELECT COUNT(*) FROM rental WHERE return_date IS NULL;

SELECT f.title, f.replacement_cost FROM film f 
JOIN inventory i ON f.film_id = i.film_id JOIN rental r ON 
i.inventory_id =r.inventory_id WHERE r.return_date IS NULL
ORDER BY f.replacement_cost DESC LIMIT 30;

SELECT f.title, f.description FROM film f
JOIN film_actor fa ON f.film_id=fa.film_id
JOIN actor a ON fa.actor_id =a.actor_id
WHERE f.description ILIKE '%sumo wrestler%' AND a.first_name ='Penelope'
AND a.last_name ='Monroe';

SELECT f.title, f.length, f.description FROM film f JOIN film_category fc ON 
f.film_id =fc.film_id JOIN category c ON fc.category_id =c.category_id
WHERE c.name ='Documentary' AND f.length < 60 AND f.rating ='R';

SELECT f.title, f.rental_rate,r.return_date From film f JOIN inventory i ON f.film_id =i.film_id
JOIN rental r ON i.inventory_id =r.inventory_id 
JOIN customer cu on r.customer_id =cu.customer_id
WHERE cu.first_name ='Matthew' AND cu.last_name ='Mahan' AND f.rental_rate >4.00
AND r.return_date BETWEEN '2005-07-28' AND '2005-08-01';

SELECT f.title, f.description, f.replacement_cost FROM film f JOIN inventory i ON f.film_id =i.film_id 
JOIN rental r ON i.inventory_id =r.inventory_id JOIN customer cu ON r.customer_id =cu.customer_id
WHERE cu.first_name ='Matthew' AND cu.last_name ='Mahan' 
AND (f.title ILIKE '%boat%' OR f.description ILIKE '%boat%')
ORDER BY f.replacement_cost DESC LIMIT 1;



