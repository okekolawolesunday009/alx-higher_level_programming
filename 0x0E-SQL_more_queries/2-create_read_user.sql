-- write a script that creates the db hbtn_0d_2
-- create user user_0d_2
-- have only selected priveleges
-- have password set to the required
-- if db exist it should not fail
-- if user exist it should not fail

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';
ALTER USER 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_02_pwd';
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
FLUSH PRIVILEGES;
