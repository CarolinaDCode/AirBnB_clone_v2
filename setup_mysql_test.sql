-- Create user hbnb_dev and add permissions.
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost'  IDENTIFIED BY 'hbnb_test';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
use hbnb_test_db;
GRANT ALL ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;