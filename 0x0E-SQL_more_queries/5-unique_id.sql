-- Create the table `unique_id` if it does not already exist
-- The `id` column is an integer with a default value of 1 and a unique constraint
-- The `name` column is a variable character string of up to 256 characters
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1,
    name VARCHAR(256),
    UNIQUE (id)
);

