#!/bin/python3

import requests
from bs4 import BeautifulSoup

base_url = "https://www.primeleague.gg/de/leagues/teams/"

class Team:
    'Create a Team Object with Primeleague ID and their matches'

    id = 0
    match = 0

    def __init__(self, id):
        self.id = id

    # TODO: only gives a soup not the match links
    def get_matches(self):
        'Retrieve all matches from the Teams site'

        response = requests.get(base_url + self.id)
        soup = BeautifulSoup(response.text, "html.parser")
        return soup

    def get_links(self):
        'A test to retrieve all links - can be deleted later'

        soup = self.get_matches()

        for link in soup.find_all('a'):
            print(link.get('href'))

    # TODO
    def get_summoners(self):
        return None
