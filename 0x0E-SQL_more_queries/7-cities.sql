-- script that creats a db eith the folloeing attributes

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (

  id INT NOT NULL AUTO_INCREMENT,
  state_id INT,
  name VARCHAR(256) NOT NULL ,
  PRIMARY KEY(id)

);
