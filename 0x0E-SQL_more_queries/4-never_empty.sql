-- Create the table `id_not_null` if it does not already exist
-- The `id` column is an integer with a default value of 1 and cannot be NULL
-- The `name` column is a variable character string of up to 256 characters
CREATE TABLE IF NOT EXISTS `id_not_null` (
    `id` INT NOT NULL DEFAULT 1,
    `name` VARCHAR(256)
);

