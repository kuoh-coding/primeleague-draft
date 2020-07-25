#!/bin/python3

import argparse

from main import *

parser = argparse.ArgumentParser()
parser.add_argument("-id", help="Set Team ID")
args = parser.parse_args()

team_id = "112031"
match_id = "598321"

print(f"===MATCHES FROM TEAMID {team_id}===")
matches = get_matches(team_id)
for match in matches:
    print(match)

print(f"===CHAMPIONS IN MATCHID {match_id}===")
match = get_champions(match_id)
for game in match:
    print(f"{game} played as {match[game]}")
