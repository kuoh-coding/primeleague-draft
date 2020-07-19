#!/bin/python3

import requests
import argparse
from bs4 import BeautifulSoup

base_url = "https://www.primeleague.gg/de/leagues/teams/"

parser = argparse.ArgumentParser()
parser.add_argument("-id", help="Set Team ID")
args = parser.parse_args()

class Team:
    'Create a Team Object with Primeleague ID and their matches'

    id = 0
    matches = 0

    def __init__(self, id):
        self.id = args.id

    def get_matches(self):
        response = requests.get(base_url + self.id)
        soup = BeautifulSoup(response.text, "html.parser")
        return soup