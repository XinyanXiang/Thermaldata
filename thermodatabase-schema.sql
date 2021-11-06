-- olympics-schema.sql: Create tables for the Olympics databese
-- Written by Xinyan Xiang, Oct 14 ,2021

CREATE TABLE measurements (
	measurement_id INTEGER,
	channel_id INTEGER,
	time_period Text
);
-- \copy measurements FROM 'measurement.csv' DELIMITER ',' CSV NULL AS 'NULL'

CREATE TABLE channels (
	id INTEGER,
	channel_name TEXT
)
-- \copy channels FROM 'channel.csv' DELIMITER ',' CSV NULL AS 'NULL'









