Select last_name, first_name, birth_date from students where students_id <= 4 ORDER BY last_name;
Select last_name, first_name, birth_date from students ORDER BY birth_date DESC LIMIT 1;
Select last_name, first_name,birth_date from students where students_id <=5 and students_id not in (2,3)