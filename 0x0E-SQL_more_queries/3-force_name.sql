-- Create the table `force_name` if it does not already exist
-- The table has two columns: `id` (an integer with a default
-- value of 0) and `name` (a non-nullable string of up to 256
-- characters with a default value of an empty string)
CREATE TABLE IF NOT EXISTS force_name (
    id INT DEFAULT 0,
    name VARCHAR(256) NOT NULL DEFAULT ''
);

