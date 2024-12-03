create database my_gym;
use my_gym;

CREATE TABLE members (
	member_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	name VARCHAR(50) NOT NULL,
    age INT NOT NULL,
	email VARCHAR(100) NOT NULL,
	phone VARCHAR(20) NOT NULL,
	join_date DATE NOT NULL,
	expiration_date DATE NOT NULL
);

CREATE TABLE WorkoutSessions (
	session_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	member_id INT NOT NULL,
	session_date DATE NOT NULL,
	session_time TIME NOT NULL,
	workout_type VARCHAR(20) NOT NULL,
	FOREIGN KEY (member_id) REFERENCES members(member_id)
);
