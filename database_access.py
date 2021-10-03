import time
import os
from mysql import connector
import mysql.connector
from mysql.connector import Error
from mysql.connector.errors import custom_error_exception
from player_stats_setup import new_dictionary as player_metrics
from colorama import Fore, Back

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(host=host_name,user=user_name,passwd=user_password, database=db_name)
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

connection = create_connection("localhost", os.environ.get('username'), os.environ.get('password'), "uva_football")
cursor = connection.cursor()
  
def get_usr_input():
    o_or_d = input("Offensive or defensive (o/d)?  ")
    player_name = input("Name of player: ")
    player_number = input("Player number: ")
    return (o_or_d, player_name, player_number)

def insert_data():
    tup = get_usr_input()
    summary = {}

    summary["name"] = tup[1]
    summary["number"] = tup[2]

    if tup[0] == "o":
        attributes = ("rushing_yards", "rushing_touchdowns", 
                        "longest_rush", "reception_yards", 
                        "recieving_touchdowns", "longest_reception", 
                        "passing_yards", "passing_touchdowns", "longest_pass")
        for a in attributes:
            value = input(a + ": ")
            summary[a] = value

        # Look up player ID with the given name and number
        player_id = get_player_id(summary['name'], summary['number'])

        query = f"INSERT INTO offensive_stats (rushing_yards, rushing_touchdowns, longest_rush, reception_yards,\
                        recieving_touchdowns, longest_reception, passing_yards, passing_touchdowns, longest_pass,\
                         player_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

        values = (summary['rushing_yards'], summary['rushing_touchdowns'], summary['longest_rush'], summary['reception_yards'],
                summary['recieving_touchdowns'], summary['longest_reception'], summary['passing_yards'], summary['passing_touchdowns'],
                summary['longest_pass'], player_id)
        cursor.execute(query, values)
        connection.commit()
        print("Database updated:\n", cursor.fetchall())

def get_player_id(name, number=None):
    if number == None:
        query = f"SELECT id FROM players WHERE name = {name}"
        cursor.execute(query)
        player_id = cursor.fetchone()[0]
    else:
        query = f"SELECT id FROM players WHERE name = {name} AND number = {number}"
        cursor.execute(query)
        player_id = cursor.fetchone()[0]
    return player_id

def get_position_id(position_name):
    query = f"SELECT id FROM positions WHERE position_name = {position_name}"
    try:
        cursor.execute(query)
        position_id = cursor.fetchone()
        return position_id
    except connection.Error as e:
        print(e)
        print("could not complete request")

def get_table(table_name):
    query = f"SELECT * FROM {table_name};"  
    cursor.execute(query)
    response = cursor.fetchall()
    return response

def delete_all_data(table_name):
    query = f"DELETE FROM {table_name} WHERE id > 0;"
    cursor.execute(query)
    connection.commit()
    print("All data succesfully deleted from "+ table_name)
    print("thanks")

def insert_player_metrics(id, player_id, position_id, metrics, keys):
    v = '%s, ' * 54 + '%s'
    query = f"INSERT INTO player_seasons_stats (id, player_id, position_id, passing_attempts, passing_completions,\
                passing_yards, passing_completion_percentage, passing_yards_per_attempt, passing_yards_per_completion, \
                passing_touchdowns, passing_interceptions, passing_rating, rushing_attempts, rushing_yards, rushing_yards_per_attempt, \
                rushing_touchdowns, rushing_long, receptions, recieving_yards, recieving_yards_per_reception, recieving_touchdowns, \
                recieving_long, punt_returns, punt_return_yards, punt_return_yards_per_attempt, punt_return_touchdowns, \
                punt_return_long, kick_returns, kick_return_yards, kick_return_yards_per_attempt, kick_return_touchdowns, \
                kick_return_long, punts, punt_yards, punt_average, punt_long, field_goals_attempted, field_goals_made, \
                field_goal_percentage, field_goals_longest_made, extra_points_attempted, extra_points_made, interceptions, \
                interception_return_yards, interception_return_touchdowns, solo_tackles, assisted_tackles, tackles_for_loss, \
                sacks, passes_defended, fumbles_recovered, fumble_return_touchdowns, quarter_back_hurries, fumbles, fumbles_lost) \
                VALUES ({v})"
    values = (id, player_id, position_id)
    for i in keys:
        if i == "Position" or i == "PositionCategory":
            pass
        else:
            values = values + (metrics[i],)

   
    cursor.execute(query, values)
    rows = cursor.fetchall()
    connection.commit()
    print("Successfully inserted player metrics")
    # Replace this lines
    show_player_stats_table()        

def show_player_stats_table():
    cursor.execute("SELECT * FROM player_seasons_stats")

    data = cursor.fetchall()
    headers = cursor.column_names
    column_outline = ""
    header_line = ""
    h_end = ""

    for header in headers:
        column_outline += "____"
        header_line += f"|{header[:1]}.."
        h_end += "----"
        values = ""
    for r in data:
        for i in r:
            if len(str(i)) == 1:
                values += " " + Fore.MAGENTA + str(i) + Fore.WHITE + " |"
            elif len(str(i)) == 2:
                values += Fore.MAGENTA + str(i) + Fore.WHITE + " |"
            elif len(str(i)) == 3:
                if i != 0.0:
                    values += Fore.MAGENTA + str(i) + Fore.WHITE + "|"
                else:
                    values += str(i) + "|"
        values += "\n"

    print(column_outline)
    print(header_line)
    print(h_end)
    print(values)
    
if __name__ == "__main__":
    print("Welcome to the UVA Football Database Interface\n")
    time.sleep(1)
    route = input("What would you like to do today?\n\
    - Insert Season Stats by player: [i]\n\
    - View Season Sats by player: [v]\n\
    - Modify data in Season Stats by player table: [m]\n\
    - Delete data in Season Stats by player table: [d]\n\
    " + Fore.GREEN + "Selection: " + Fore.RESET)
    
    if route.lower() == "i":
        usr_input = input("Retrieving data from SportsDataio to insert in database. (y) to continue (q) to quit: ")
        if usr_input.lower() == "y":
            r = get_table("player_seasons_stats")
            if len(r) > 3:
                lvl_2 = input("Player metrics had already been inserted. Would you like to see the table? (y/n) ")
                if lvl_2.lower() == "y":
                    show_player_stats_table()
                else:
                    print("thank you")
            else:
                id = 1
                for k in player_metrics:
                    try:
                        player_id = get_player_id(repr(k))
                        position_id = get_position_id(repr(player_metrics[k]['Position']))
                        if position_id != None:
                            insert_player_metrics(id, player_id, position_id[0], player_metrics[k], player_metrics[k].keys())
                            id +=1
                            
                    except connector.Error as e :
                        print("could not retrieve player id from databse")
                        print(e.msg)
    elif route.lower() == "v":
        print("Getting the table now")
        show_player_stats_table()
    elif route.lower() == "d":
        lvl_1 = input("would you like to delete all data in player_seasons_stats table? (y/n) ")
        if lvl_1.lower() == "y":
            delete_all_data("player_seasons_stats")

   
    
    


