-- Create the table `id_not_null` if it does not already exist
-- The `name` column is a variable character string of up to 256 characters
-- The `id` column is an integer with a default value of 1 and cannot be NULL
CREATE TABLE IF NOT EXISTS `id_not_null` (
    `id` INT NOT NULL DEFAULT 1 PRIMARY KEY,
    `name` VARCHAR(256)
);
