-- Create the database `hbtn_0d_usa` if it does not already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Switch to the `hbtn_0d_usa` database
USE hbtn_0d_usa;

-- Create the table `states` if it does not already exist
-- The `id` column is an integer, unique, not null, and auto-incrementing
-- The `name` column is a non-nullable string of up to 256 characters
-- The primary key is the `id` column
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT UNIQUE,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);

