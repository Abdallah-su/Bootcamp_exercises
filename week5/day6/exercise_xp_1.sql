SELECT * FROM language;
SELECT language.name, film.title, film.description 
FROM film LEFT JOIN language ON film.language_id =language.language_id;

SELECT language.name, film.title, film.description 
FROM
language LEFT JOIN film ON language.language_id =film.language_id;
CREATE TABLE new_film (id SERIAL PRIMARY KEY,film_name  VARCHAR(30) NOT NULL);
INSERT INTO new_film(film_name)
VALUES('Commando'),('Inception'),('Be a man')
CREATE TABLE customer_review (
    review_id SERIAL PRIMARY KEY,
    film_id INTEGER REFERENCES new_film(id) ON DELETE CASCADE,
    language_id INTEGER REFERENCES language(language_id),
    title VARCHAR(255) NOT NULL,
    score SMALLINT CHECK (score >= 1 AND score <= 10),
    last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    review_text TEXT);
INSERT INTO customer_review (film_id, language_id, title, score, review_text)
VALUES 
(1, 1, 'Say yes!', 9, 'Really enjoyed the plot and the acting.'),
(2, 1, 'my type of man', 4, 'The pacing was a bit slow for my taste.');
-- DELETE FROM new_film where id =1;
SELECT * FROM customer_review;
