-- creates the database hbtn_0d_2 and the user user_0d_2
-- Ensure the database hbtn_0d_2 exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Ensure the user 'user_0d_2'@'localhost' exists with the specified password
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant SELECT privileges on the database hbtn_0d_2 to the user 'user_0d_2'@'localhost'
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Reload the privileges to ensure the changes take effect
FLUSH PRIVILEGES;

