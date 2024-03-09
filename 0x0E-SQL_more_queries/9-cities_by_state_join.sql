-- lists all cities contained in the database hbtn_0d_usa.
-- Each record should display: cities.id - cities.name - states.name
-- Results must be sorted in ascending order by cities.id
-- You can use only one SELECT statement
<<<<<<< HEAD
SELECT cities.id, cities.name, states.name FROM cities JOIN states ORDER BY cities.id;
=======
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON cities.state_id = states.id
ORDER BY cities.id;
>>>>>>> 7ffbaf1be0c5bca9127b9c9689cbca622fea8ead
