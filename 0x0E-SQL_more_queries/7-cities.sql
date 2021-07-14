-- This scrip creates the database hbtn_0d_usa and the table cities
-- The id column INT unique, auto generated, can’t be null and is a primary key
-- The state_id column INT, can’t be null and must be a FOREIGN KEY that
-- references to id of the states table
-- The name column VARCHAR(256) can’t be null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (id INT UNIQUE NOT NULL PRIMARY KEY AUTO_INCREMENT,
state_id INT NOT NULL, FOREIGN KEY(id) REFERENCES states(id),
name VARCHAR(256) NOT NULL);
