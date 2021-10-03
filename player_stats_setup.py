import requests
from set_credential import *
url = "https://api.sportsdata.io/v3/cfb/stats/json/PlayerSeasonStatsByTeam/2021/vir"
headers = {"Ocp-Apim-Subscription-Key" : "e76b29b3cc1e46a7b28c3346389bead4"}
r = requests.get(url, headers=headers)
stats_json = r.json()
new_dictionary = {}
stats_list = []
# get everything except statid, teamid, playerid, seasontype, season, team, globalteamid, updated, created, games, and fantasy points. 
no_go = ['StatID', 'TeamID', 'PlayerID', 'SeasonType', 'Season', 'Name', 'Team', 'GlobalTeamID', 'Updated', 'Created', 'Games', 'FantasyPoints']
for i in stats_json:
    new_key = i["Name"]
    new_dictionary[new_key] = i

for i in new_dictionary.values():
    for ng in no_go:
        i.pop(ng)

