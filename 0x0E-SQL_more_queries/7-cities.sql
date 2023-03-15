-- creates the database hbtn_0d_usa
-- create table cities
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`cities` (
	PRIMARY KEY(`id`),
	`id` INT	NOT NULL AUTO_INCREMENT,
	`state_id` INT, 
	`name` VARCHAR(256) NOT NULL, FOREIGN KEY (id) REFERENCES states(id));
