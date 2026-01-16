create database bootcamp;
create table students (student_id Serial primary key, last-name text not null, first_name text not null, birth_date date not null);
insert  into students(last_name, first_name, birth_date)
values ('Benichou', 'Marc', '1998-11-02' ), ('Cohen', 'Yoan' '2010-12-03'), ('Benichou', 'Lea' '1987-07-27'),('Dux', 'Amelia' '1996-04-07'), ('Grez', 'David', '2003-06-14'),('Simpson', 'Omer', '1980-10-03');
select * from students;
Select last_name, first_name from students ;
Select last_name, first_name from students where students_id = 2;
Select last_name, first_name from students where last_name = 'Benichou' and first_name = 'Marc';
Select last_name, first_name from students where last_name ='benichou' or first_name = 'Marc';
Select last_name, first_name from students where first_name ilike '%a%';
Select last_name, first_name from students where first_name ilike 'a%';
Select last_name, first_name from students where first_name ilike '%a';
Select last_name, first_name from students where first_name ilike '_%a';
Select last_name, first_name from students where students_id = 1 and students_id = 3;
Select last_name, first_name from students where birth_date >= '2000-01-01';

