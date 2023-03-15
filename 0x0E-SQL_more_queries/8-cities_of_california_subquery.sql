-- lists all the cities of California that can be found in the database hbtn_0d_usa
-- Results must be sorted in ascending order by cities.id
-- ot allowed to use the JOIN
USE hbtn_0d_usa;
SELECT DISTINCT name FROM states
WHERE name = California;
ORDER BY cities.id ASC;

