#!/bin/python3

import argparse

from main import *

parser = argparse.ArgumentParser()
parser.add_argument("-id", help="Set Team ID")
args = parser.parse_args()

#team_id = "112031"
team_id = "136156"
match_id = "598321"

print(f"===OP.GG MULTILINK OF TEAMID {team_id}===")
print(generate_opgg(team_id))

print(f"===PRESENCE TEST===")
for key, value in count_to_dict(get_champion_presence(team_id)).items():
    print(f"{key} : {value}")

print(f"===CHAMPIONCOUNT FROM ALL MATCHES OF TEAMID {team_id}===")
for key, value in count_to_dict(get_champions_of_team(team_id)).items():
    print(f"{key} : {value}")

print(f"===BANS TEST===")
for key, value in count_to_dict(get_all_bans_against(team_id)).items():
    print(f"{key} : {value}")

print(f"===BANS AGAINST TEAMID {team_id} IN MATCH {match_id}===")
print(get_bans_against(match_id, team_id))

print(f"===BANS IN MATCH {match_id}===")
for key, value in get_all_bans(match_id).items():
    print(f"{key} : {value}")

print(f"===MATCHS FROM TEAMID {team_id}===")
matches = get_matches(team_id)
for match in matches:
    print(match)

print(f"===CHAMPIONS IN MATCH {match_id}===")
match = get_champions(match_id)
for game in match:
    print(f"{game} played as {match[game]}")

print(f"===CHAMPIONS FROM MATCHES OF TEAMID {team_id}===")
for match in get_matches(team_id):
    print(get_champions(match))