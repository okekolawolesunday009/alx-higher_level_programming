-- writing a script that that wile show all the records where name   califonia



SELECT * FROM cities
WHERE state_id = (
SELECT id FROM states WHERE name ='California')
ORDER BY id;

