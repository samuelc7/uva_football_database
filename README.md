# Overview

The software I wrote is for an app that I am building. I am building a Virginia Football app that will help bring the fanbase together and provide information regarding the team.
A big part of the app will deal with the player stats so in this project I created a sql database with each of the players statistics for this football season. I also provided a way to 
easily pull the changing data and insert it into the database - all stats change weekly so this part is essential to my project. 

I created a simple interface for how to determine what needs to happen with the database that I created. If the insert finctionality is selected, a pull request is made to [Sportsdataio](https://sportsdata.io/developers/api-documentation/ncaa-football#/sports-data) to pull all of the most recent stats of each player. Then a sql query is used to insert all of this data in the correct table. 
I also made a deleting option to be able to quickly delete all values in a table - I found that for my purposes for now, it's easier to delete all the data then insert new data instead of modifying everything. I also created a viewing option to view the current data in the player_seasons_stats.

I also made more tables in the database for the future. There's the classes, coaches, high_schools, hometowns, players, and positions tables all ready to be used. 

To run the program, make sure to have the correct credentials to the database in the database_access.py file and then hit run. 


[Software Demo Video](http://youtube.link.goes.here)

# Relational Database

I am using a SQL relational database with information about all of the players on the Virginia Football team. I created the 
data base using sql scripts in mysql workbench. I also used sql queries to populate all of the tables. 

The most important table and the one that will be used most is the player_seasons_stats. This contains all of the stats of each player and is the only one set up with the user interface so far. 
Other important tables:
* Coaches - has the id, name, and name of all the coaches
* Hometowns - all the hometowns that the players are from
* Positions - all the different positions on the football team
* Players - player information
  
# Development Environment

* VSCode
* MySQLWorkBench
  
* The language used for the main interface is python
* Mysql python library used: 
    * helps access databases
    * executes sql queries and returns data from databases
* Colorama python library also used:
    * helps change text color in terminal 
  

# Useful Websites

* [dev.mysql.com](https://dev.mysql.com/doc/connector-python/en/connector-python-introduction.html)
* [sportsdata.io](https://sportsdata.io/members/subscriptions)

# Future Work

* Add more functionality for the user to be able to modify data in the database
* Create weekly automation to populate database after each football game
* Creat a gui to simplify the user's experience. 