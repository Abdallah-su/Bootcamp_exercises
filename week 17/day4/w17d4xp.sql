SELECT m.title, g.genre_name, RANK() OVER (PARTITION BY g.genre_name ORDER BY m.popularity DESC) 
AS rankings FROM movies.movie m JOIN movies.movie_genres mg ON m.movie_id =mg.movie_id 
JOIN movies.genre g ON mg.genre_id =g.genre_id;

SELECT pc.company_name, m.title, m.revenue, 
NTILE(4) OVER(PARTITION BY pc.company_name ORDER BY m.revenue DESC) AS quartile FROM movies.movie m 
JOIN movies.movie_company mc ON m.movie_id = mc.movie_id 
JOIN movies.production_company pc ON mc.company_id =pc.company_id WHERE m.revenue 
>0;

SELECT g.genre_name, m.title, m.budget, 
SUM(m.budget) OVER (PARTITION BY g.genre_name ORDER BY m.title 
ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)AS running_total_budget
FROM movies.movie m 
JOIN movies.movie_genres mg ON m.movie_id =mg.movie_id
JOIN movies.genre g ON mg.genre_id =g.genre_id WHERE m.budget >0;

SELECT DISTINCT g.genre_name, FIRST_VALUE(m.title) 
OVER (partition BY g.genre_name ORDER BY m.release_date DESC ) AS movie_title, m.release_date 
FROM  movies.movie m JOIN movies.movie_genres mg ON m.movie_id =mg.movie_id 
JOIN movies.genre g ON mg.genre_id =g.genre_id; 

SELECT p.person_name, DENSE_RANK() OVER (ORDER BY COUNT(m.movie_id) DESC) AS rankings,
COUNT(mc.movie_id) AS num_movies FROM movies.person p 
JOIN movies.movie_cast mc ON p.person_id = mc.person_id
JOIN movies.movie m ON mc.movie_id =m.movie_id
GROUP BY p.person_name ORDER BY num_movies DESC;

WITH Director_movie_rating AS (SELECT p.person_name AS director, AVG(m.vote_average) as avg_ratings
FROM movies.person p
JOIN movies.movie_crew mc ON p.person_id = mc.person_id
JOIN movies.movie m ON mc.movie_id =m.movie_id WHERE mc.job ='Director' GROUP BY p.person_name )

SELECT director, avg_ratings, RANK() OVER (ORDER BY avg_ratings DESC) AS rank FROM Director_movie_rating ;

SELECT p.person_name, SUM(m.revenue) OVER (ORDER BY p.person_name ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW ) 
FROM movies.person p JOIN movies.movie_cast mc ON p.person_id =mc.person_id
JOIN movies.movie m ON mc.movie_id =m.movie_id;

WITH Director_budget AS (SELECT DISTINCT p.person_name AS Director, m.budget as budget
FROM movies.person p JOIN movies.movie_crew mc ON p.person_id =mc.person_id
JOIN movies.movie m ON mc.movie_id =m.movie_id 
WHERE mc.job ='Director' AND m.budget > 0)
SELECT Director,
SUM(budget) OVER (ORDER BY Director ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW ) AS total_budget
From Director_budget ORDER BY total_budget DESC;
