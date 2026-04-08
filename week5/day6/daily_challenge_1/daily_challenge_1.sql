CREATE TABLE customer (id SERIAL PRIMARY KEY, first_name text NOT NULL, last_name text NOT NULL);
CREATE TABLE customer_profile (id SERIAL PRIMARY KEY, isLoggedin BOOLEAN DEFAULT False, 
customer_id INTEGER UNIQUE REFERENCES customer(id) ON DELETE CASCADE);
INSERT INTO customer(first_name, last_name) VALUES
('John', 'Doe'), ('Jerome', 'Dalu'),('Lea', 'Rive');
INSERT INTO customer_profile (isLoggedin, customer_id) VALUES
(True, (SELECT id FROM customer where first_name = 'John' LIMIT 1));
INSERT INTO customer_profile(isLoggedin, customer_id) values
(False, (SELECT id FROM customer WHERE first_name ='Jerome' LIMIT 1));
SELECT * FROM customer_profile;
SELECT COUNT(*) FROM customer_profile WHERE isLoggedin = false;
