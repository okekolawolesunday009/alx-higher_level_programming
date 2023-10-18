-- scipt that creates a db if not exist corelation to the previous task
-- id cannot be null while create the table 
--  script should not fail during or after runtime

CREATE TABLE IF NOT EXISTS id_not_null
(

 id INT NOT NULL,
 name VARCHAR(256)
);
