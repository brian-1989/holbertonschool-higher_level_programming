-- This scrip creates the database hbtn_0d_usa and the table states
-- The id column INT unique, auto generated, can’t be null and is a primary key
-- The name column name VARCHAR(256) can’t be null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (id INT NOT NULL PRIMARY KEY AUTO_INCREMENTE,
name VARCHAR(256) IS NOT NULL);
