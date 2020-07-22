#!/bin/python3

import requests
from bs4 import BeautifulSoup

class Team:
    def __init__(self, id):
        self.id = id

    def get_soup(self, uri: str):
        'Get a soup from the website'

        response = requests.get(uri + self.id)
        soup = BeautifulSoup(response.text, "html.parser")
        return soup


    def generate_opgg(self):
        'Generate a op.gg link with all summoners from the team'

        team_soup = self.get_soup("https://www.primeleague.gg/de/leagues/teams/")

        op_link = "https://euw.op.gg/multi/query="

        for i in team_soup.find_all("span", title="League of Legends » LoL Summoner Name (EU West)"):
            summoner = i.get_text()
            print(summoner)
            op_link += ("%2C" + summoner.replace(" ",""))

        print(op_link)


    # TODO: should return an array with all matches from the team
    def get_matches(self):
        return None


    def get_champions(self):
        'returns a dictionary with summoners and champions'
        
        match_soup = self.get_soup("https://www.primeleague.gg/de/leagues/matches/")

        'extracts the summoner names'
        summoners = []
        for i in match_soup.find_all("div", "submatch-lol-player-name"):
            summoners.append(i.text)

        'extracts the played champions'
        champions = []
        for i in match_soup.find_all("img", "img-player-hero"):
            champions.append(i.get("title"))

        return dict(zip(summoners,champions))
    

        
