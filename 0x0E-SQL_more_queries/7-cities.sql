-- Create the database `hbtn_0d_usa` if it does not already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the `hbtn_0d_usa` database
USE hbtn_0d_usa;

-- Create the table `cities` if it does not already exist
-- The `id` column is an integer, unique, not null, and auto-incrementing
-- The `state_id` column is an integer and not null
-- The `name` column is a non-nullable string of up to 265 characters
-- The primary key is the `id` column
-- There is a foreign key constraint on `state_id` referencing the
-- `id` column of the `states` table
CREATE TABLE IF NOT EXISTS cities (
    id INT NOT NULL AUTO_INCREMENT UNIQUE,
    state_id INT NOT NULL,
    name VARCHAR(265) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) REFERENCES states(id)
);

