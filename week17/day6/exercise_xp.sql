CREATE TABLE IF NOT EXISTS df_employee AS 
SELECT
    s.employee_id || '_' || s.date AS id,
    DATE(SUBSTR(s.date, 7, 4) || '-' || SUBSTR(s.date, 4, 2) || '-' || SUBSTR(s.date, 1, 2)) AS month_year,
    s.employee_id,
    s.employee_name,
    e.gen_m_f     AS gender,
    e.age,
    s.salary,
    f.function_group,
    c.company_name,
    c.company_city,
    c.company_state,
    c.company_type,
    c.const_site_categ
FROM salaries s
LEFT JOIN employees e ON e.comp_code_emp = s.employee_id
LEFT JOIN functions f ON f.function_code     = s.func_code
LEFT JOIN companies c ON c.company_name      = s.comp_name;
SELECT * FROM df_employee;
UPDATE df_employee set id= TRIM(id),
employee_id = TRIM (employee_id),
employee_name =TRIM(employee_name),
gender = TRIM(gender),
age=TRIM(age),
salary=TRIM(salary),
function_group= TRIM(function_group),
company_name = TRIM(company_name),
company_city=TRIM(company_city),
company_state = TRIM(company_state),
company_type = TRIM(company_type),
const_site_categ = TRIM(const_site_categ);

SELECT * FROM df_employee WHERE id IS NULL OR employee_id IS NULL OR employee_name IS NULL OR gender IS NULL OR age IS NULL
OR salary IS NULL OR function_group IS NULL OR company_name IS NULL OR company_city IS NULL OR company_state IS NULL
OR company_type IS NULL OR const_site_categ IS NULL;

DELETE FROM df_employee WHERE salary =' ';

SELECT company_name, COUNT(employee_id) AS total_employees FROM df_employee GROUP BY company_name;

select company_city, COUNT(employee_id) as total_employees, 
(COUNT(employee_id)*100 / (SELECT COUNT(employee_id) FROM df_employee)) as percentage from df_employee GROUP BY company_city;
 
 SELECT strftime('%Y-%m',month_year) AS months, COUNT(employee_id) AS total_employees FROM df_employee GROUP BY months
 ORDER by months;
 
 select count(employee_id)/COUNT (DISTINCT strftime('%Y-%m',month_year)) as average_per_month 
 from df_employee ;
 
 
 with employee_count as (select DISTINCT strftime('%Y-%m',month_year) AS month, 
 COUNT (employee_id) as value 
 from df_employee GROUP by month)
 select (select month from employee_count order by value ASC limit 1) as min_month, MIN(value) as min_value, 
 (select month from employee_count order by value desc limit 1) as max_month, MAX(value) AS max_value 
 from employee_count;
 
 select function_group, count(employee_id)/COUNT (DISTINCT strftime('%Y-%m',month_year)) as average_per_month 
 from df_employee GROUP by function_group ;
 
 SELECT(SUM(salary)/COUNT (DISTINCT strftime('%Y-%m',month_year)))*12 as annual_average_salary
  from df_employee  
 