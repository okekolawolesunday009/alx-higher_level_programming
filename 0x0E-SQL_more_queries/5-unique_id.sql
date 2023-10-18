-- script that creares unique id in a table named'unique_id'

CREATE TABLE IF NOT EXISTS unique_id
(

  id INT UNIQUE,
  name VARCHAR(256)
);
