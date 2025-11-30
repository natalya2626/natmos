SELECT * FROM netflix_shows;

SELECT title, release_year
FROM netflix_shows
WHERE type = 'Movie';



SELECT title, director
FROM netflix_shows
WHERE type = 'Show' AND rating > 8.0 ;

SELECT id, type, description
FROM records
WHERE description ILIKE '%love%';

SELECT *
FROM records
ORDER BY release_date DESC
LIMIT 10;
