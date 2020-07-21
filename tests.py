#!/bin/python3

import argparse

# local
from main import Team

parser = argparse.ArgumentParser()
parser.add_argument("-id", help="Set Team ID")
args = parser.parse_args()


eko = Team(args.id)

eko.generate_opgg()
