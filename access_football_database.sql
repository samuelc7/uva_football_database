/* CREATE TABLE players (id INT NOT NULL AUTO_INCREMENT, name VARCHAR(45), number INT, height VARCHAR(45), weight INT, PRIMARY KEY ( id )); 
SHOW TABLES; 

LOAD DATA LOCAL INFILE "/Users/samuelcummings/Desktop/School/Fall_2021/cse310/sprint1/new_players.txt" INTO TABLE players;

UPDATE players SET number = null WHERE number = 0 AND name != "Jelani Woods";

SELECT * FROM players;

CREATE TABLE hometowns (id INT NOT NULL AUTO_INCREMENT, city VARCHAR(45), state VARCHAR(45), country VARCHAR(45), PRIMARY KEY ( id ));

CREATE TABLE classes (id INT NOT NULL AUTO_INCREMENT, name VARCHAR(45), PRIMARY KEY ( id ));

CREATE TABLE defensive_stats (id INT NOT NULL AUTO_INCREMENT, sacks INT, interceptions INT, tackles INT, PRIMARY KEY ( id ));

CREATE TABLE offensive_stats (id INT NOT NULL AUTO_INCREMENT, rushing_yards INT, rushing_touchdowns INT, longest_rush INT, reception_yards INT, recieving_touchdowns INT, longest_reception INT, passing_yards INT, passing_touchdowns INT, longest_pass INT, PRIMARY KEY ( id ));

CREATE TABLE positions (id INT NOT NULL AUTO_INCREMENT, position_name VARCHAR(3), PRIMARY KEY ( id ));

CREATE TABLE coaches (id INT NOT NULL AUTO_INCREMENT, title VARCHAR(45), PRIMARY KEY ( id ));

CREATE TABLE high_schools (id INT NOT NULL AUTO_INCREMENT, name VARCHAR(45), PRIMARY KEY ( id ));

ALTER TABLE coaches ADD name VARCHAR(45);

SET GLOBAL local_infile = 1;

LOAD DATA LOCAL INFILE "/Users/samuelcummings/Desktop/School/Fall_2021/cse310/sprint1/new_coaches.txt" INTO TABLE coaches;
 
LOAD DATA LOCAL INFILE "/Users/samuelcummings/Desktop/School/Fall_2021/cse310/sprint1/hometowns.txt" INTO TABLE hometowns;

LOAD DATA LOCAL INFILE "/Users/samuelcummings/Desktop/School/Fall_2021/cse310/sprint1/classes.txt" INTO TABLE classes;

LOAD DATA LOCAL INFILE "/Users/samuelcummings/Desktop/School/Fall_2021/cse310/sprint1/high_schools.txt" INTO TABLE high_schools;

LOAD DATA LOCAL INFILE "/Users/samuelcummings/Desktop/School/Fall_2021/cse310/sprint1/positions.txt" INTO TABLE positions;

ALTER TABLE positions
MODIFY position_name VARCHAR(10);

LOAD DATA LOCAL INFILE "/Users/samuelcummings/Desktop/School/Fall_2021/cse310/sprint1/positions.txt" INTO TABLE positions;

*/
SELECT * FROM offensive_stats;