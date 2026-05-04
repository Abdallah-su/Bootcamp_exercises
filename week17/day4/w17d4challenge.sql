WITH budget_growth_rate AS (SELECT pc.company_name AS company, m.budget AS budget, m.release_date AS release_date,
((m.budget -LAG(m.budget) OVER 
(PARTITION BY pc.company_name ORDER BY m.release_date))/NULLIF(LAG(m.budget) 
OVER (PARTITION BY pc.company_name ORDER BY m.release_date ),0))*100
AS budget_growth
FROM movies.production_company pc JOIN movies.movie_company mc 
ON pc.company_id =mc.company_id JOIN movies.movie m ON mc.movie_id =m.movie_id)
SELECT DISTINCT company, AVG(budget_growth) OVER (PARTITION  BY company ORDER BY release_date) AS average_growth 
FROM budget_growth_rate;

WITH global_average AS(SELECT p.person_name AS actor, m.movie_id AS movie_id, m.vote_average AS rating,
AVG(m.vote_average) OVER () AS avg_ratings
FROM movies.person p
JOIN movies.movie_cast mc ON p.person_id=mc.person_id JOIN movies.movie m ON mc.movie_id=m.movie_id),

highly_rated_movies AS (SELECT actor, COUNT(movie_id) AS total_movies_high 
FROM global_average WHERE rating >avg_ratings GROUP BY actor)

SELECT actor, total_movies_high,
RANK() OVER (ORDER BY total_movies_high DESC) AS rankings FROM highly_rated_movies;


SELECT g.genre_name,m.title,m.revenue,
AVG(m.revenue) OVER 
(PARTITION BY g.genre_name ORDER BY m.release_date ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS rolling_average
FROM movies.genre g JOIN movies.movie_genres mg ON g.genre_id =mg.genre_id
JOIN movies.movie m ON mg.movie_id =m.movie_id WHERE m.revenue >0;


WITH Movie_Rankings AS (
    SELECT 
        k.keyword_name AS series,
        m.title AS movie_title,
        m.revenue,
        -- Use RANK to identify the #1 movie within each keyword/series
        RANK() OVER (
            PARTITION BY k.keyword_name 
            ORDER BY m.revenue DESC
        ) AS revenue_rank
    FROM movies.keyword k
    JOIN movies.movie_keywords mk ON k.keyword_id = mk.keyword_id
    JOIN movies.movie m ON mk.movie_id = m.movie_id
    WHERE m.revenue > 0
)
SELECT 
    series, 
    movie_title, 
    revenue
FROM Movie_Rankings
WHERE revenue_rank = 1; -- This picks the "Highest Revenue Movie"