-- Create table 'id_not_null If table is not already exists, script should not fail
CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT 1, name VARCHAR(256));
