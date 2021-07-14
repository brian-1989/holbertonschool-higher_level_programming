-- This scrip creates the database hbtn_0d_2 and the user hbtn_0d_2
-- with only permission of SELECT in the database hbtn_0d_2
CREATE DATABASE IF NO EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
