-- script that creates atable force_name on the mysql db server
-- force_name desc tanle 
-- 	id INT,
--      name VARCHAR(256)
-- scrippt should not fail for both the DB and the table creation.


CREATE TABLE IF NOT EXISTS force_name
(
        id INT,
        name VARCHAR(256) NOT NULL
);
