-- lists all the cities of California that can be found in the database hbtn_0d_usa.
-- The states table contains only one record where name = California (but the id can be different, as per the example)
-- Results must be sorted in ascending order by cities.id
<<<<<<< HEAD
SELECT id, name FROM cities WHERE state_id = (SELECT id from states WHERE name = "California") ORDER BY id;
=======
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = "California") ORDER BY id;
>>>>>>> 7ffbaf1be0c5bca9127b9c9689cbca622fea8ead
