-- script that creates a db hbtn_0d_usa and a table states in the db
-- scipt must nou fail id db exists and the table also sbould not fail

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states
(
   id INT NOT NULL AUTO_INCREMENT,
   name VARCHAR(256) NOT NULL,
PRIMARY KEY(id),
UNIQUE(id)

);
