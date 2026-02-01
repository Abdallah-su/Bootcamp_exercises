SELECT * FROM actor;
SELECT COUNT(first_name)FROM actor;
INSERT INTO actor(first_name)
VALUES('Van')
--it didn't add because last_name has not null constraint