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

CREATE TABLE Book (book_id SERIAL PRIMARY KEY, title text NOT NULL, author text NOT NULL);
INSERT INTO Book(title, author) VALUES
('Alice In Wonderland', 'Lewis Carroll'),
('Harry Potter', 'J.K Rowling'),
('To kill a mockingbird', 'Harper Lee');

CREATE TABLE Student(student_id SERIAL PRIMARY KEY, name TEXT NOT NULL UNIQUE , age INTEGER CHECK(age<=15));
INSERT INTO Student(name, age) VALUES
('John', 12),('Lera', 11), ('Patrick', 10),('Bob', 14);

CREATE TABLE Library(book_id INTEGER REFERENCES Book(book_id) ON DELETE CASCADE ON UPDATE CASCADE,
student_id INTEGER REFERENCES Student(student_id) ON DELETE CASCADE ON UPDATE CASCADE,
borrowed_date DATE );

INSERT INTO Library(book_id, student_id, borrowed_date) VALUES
((SELECT book_id FROM Book WHERE title ='Alice In Wonderland'),(SELECT student_id
FROM Student WHERE name ='John'), '2022-02-15' );
INSERT INTO Library(book_id, student_id, borrowed_date) VALUES
((SELECT book_id FROM Book WHERE title ='To kill a mockingbird'),(SELECT student_id
FROM Student WHERE name ='Bob'), '2021-03-03' );
INSERT INTO Library(book_id, student_id, borrowed_date) VALUES
((SELECT book_id FROM Book WHERE title ='Alice In Wonderland'),(SELECT student_id
FROM Student WHERE name ='Lera'), '2021-05-23' );
INSERT INTO Library(book_id, student_id, borrowed_date) VALUES
((SELECT book_id FROM Book WHERE title ='Harry Potter'),(SELECT student_id
FROM Student WHERE name ='Bob'), '2021-08-12' );

SELECT * FROM Library;
SELECT s.name, b.title FROM Student s JOIN Library l ON s.student_id=l.student_id
JOIN Book b ON l.book_id =b.book_id;
SELECT AVG(s.age) FROM Student s JOIN Library l ON s.student_id= l.student_id
JOIN Book b ON l.book_id =b.book_id 
WHERE b.title = 'Alice In Wonderland';
DELETE FROM Student where name ='Bob';
SELECT * FROM Library;
--anything related to Bob was deleted from the junction

