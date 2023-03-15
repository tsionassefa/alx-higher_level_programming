--  creates the table unique_id
-- id INT with the default value 1 and must be unique
DROP TABLE IF EXISTS 'unique_id';
CREATE TABLE 'unique_id' (id INT(1) UNIQUE, name VARCHAR(256)); 
