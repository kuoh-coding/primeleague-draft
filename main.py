#!/bin/python3

import requests
from bs4 import BeautifulSoup

class Team:
    def __init__(self, id):
        self.id = id

    def get_soup(self):
        'Get a soup from the website'

        prime_url = "https://www.primeleague.gg/de/leagues/teams/"
        response = requests.get(prime_url + self.id)
        soup = BeautifulSoup(response.text, "html.parser")
        return soup


    def generate_opgg(self):
        'Generate a op.gg link with all summoners from the team'

        soup = self.get_soup()

        op_link = "https://euw.op.gg/multi/query="
        summonerlist = soup.find_all('span', title="League of Legends » LoL Summoner Name (EU West)")

        for i in soup.find_all('span', title="League of Legends » LoL Summoner Name (EU West)"):
            summoner = i.get_text()
            print(summoner)
            op_link += ("%2C" + summoner.replace(" ",""))

        print(op_link)


    # TODO: should return an array with all matches from the team
    def get_matches(self):
        return None
