#!/bin/python3

import argparse

# local
from main import Team

parser = argparse.ArgumentParser()
parser.add_argument("-id", help="Set Team ID")
args = parser.parse_args()

#eko team id: 112031
#test match id: 598300
id = "598300"
eko = Team(id)



