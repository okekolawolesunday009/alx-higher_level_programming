--  selects the following parameters in the cites.id

SELECT cities.id, cities.name  states.name FROM cities 
INNER JOIN states ON cities.id = states.id
ORDER BY cities.id;  
