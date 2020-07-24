#!/bin/python3

import requests
from bs4 import BeautifulSoup

pl_teams = "https://www.primeleague.gg/de/leagues/teams/"
pl_matches = "https://www.primeleague.gg/de/leagues/matches/"


def get_soup(uri: str):
    'Get a soup from uri'

    response = requests.get(uri)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup


def generate_opgg(team_id: str):
    'Generate a op.gg link with all summoners from the team'

    team_soup = get_soup(pl_teams + team_id)
    op_link = "https://euw.op.gg/multi/query="

    for span in team_soup.find_all("span", title="League of Legends » LoL Summoner Name (EU West)"):
        summoner = span.get_text()
        op_link += ("%2C" + summoner.replace(" ",""))

    return op_link


def get_matches(team_id: str):
    'Generate an array with links to all played games'

    team_soup = get_soup(pl_teams + team_id)

    match_history = []
    table = team_soup.find_all("td", "col-3 col-text-right")
    for row in table:
        match = row.find("a","table-cell-container")
        link = match.get("href")
        match_history.append(link)

    return match_history


def get_champions(match_id: str):
    'returns a dictionary with summoners and champions'

    match_soup = get_soup(pl_matches + match_id)

    'extracts the summoner names'
    summoners = []
    for i in match_soup.find_all("div", "submatch-lol-player-name"):
        summoners.append(i.text)

    'extracts the played champions'
    champions = []
    for i in match_soup.find_all("img", "img-player-hero"):
        champions.append(i.get("title"))

    if summoners or champions:
        return dict(zip(summoners, champions))
