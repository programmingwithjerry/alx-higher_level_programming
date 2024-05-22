-- Ensure the user exists before trying to create it
-- Create a user 'user_0d_1'@'localhost' with password
-- 'user_0d_1_pwd' if it does not already exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges to 'user_0d_1'@'localhost'
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Reload the privileges to ensure the changes take effect
FLUSH PRIVILEGES;

