create database bootcamp;
create table students (student_id Serial primary key, last_name text not null, 
first_name text not null, birth_date date not null);
INSERT INTO students(last_name, first_name, birth_date)
VALUES ('Benichou', 'Marc', '1998-11-02' ), ('Cohen', 'Yoan', '2010-12-03'),
 ('Benichou', 'Lea' ,'1987-07-27'),('Dux', 'Amelia', '1996-04-07'), 
 ('Grez', 'David', '2003-06-14'),('Simpson', 'Omer', '1980-10-03');
INSERT  INTO students (last_name, first_name, birth_date)
VALUES ('Suallah', 'Abdallah', '2001-09-23'); 
SELECT * FROM students;
SELECT last_name, first_name FROM students; ;
SELECT last_name, first_name FROM students WHERE student_id = 2;
SELECT last_name, first_name FROM students WHERE last_name = 'Benichou' AND first_name = 'Marc';
SELECT last_name, first_name FROM students WHERE last_name ='Benichou' OR first_name = 'Marc';
SELECT last_name, first_name FROM students WHERE first_name ILIKE '%a%';
SELECT last_name, first_name FROM students WHERE first_name ILIKE 'a%';
SELECT last_name, first_name FROM students WHERE first_name ILIKE '%a';
Select last_name, first_name from students where first_name ilike '_%a';
SELECT last_name, first_name FROM students WHERE student_id = 1 OR student_id = 3;
SELECT * FROM students WHERE birth_date >= '2000-01-01';

