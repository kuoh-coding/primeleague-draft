#!/bin/python3

import requests
import re
from bs4 import BeautifulSoup
from collections import Counter
import collections, functools, operator

pl_teams = "https://www.primeleague.gg/de/leagues/teams/"
pl_matches = "https://www.primeleague.gg/de/leagues/matches/"


def get_soup(uri: str):
    'Get a soup from uri'

    response = requests.get(uri)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup

def get_summoners(team_id: str):
    summoners = []
    team_soup = get_soup(pl_teams + team_id)

    for span in team_soup.find_all("span", title="League of Legends » LoL Summoner Name (EU West)"):
        summoner = span.get_text().lower()
        summoners.append(summoner)
    return summoners


def generate_opgg(team_id: str):
    'Generate a op.gg link with all summoners from the team'

    op_link = "https://euw.op.gg/multi/query="

    for summoner in get_summoners(team_id):
        op_link += ("%2C" + summoner.replace(" ",""))

    return op_link


def get_matches(team_id: str):
    'Generate an array with IDs to all played games'

    team_soup = get_soup(pl_teams + team_id)

    match_history = []
    table = team_soup.find_all("td", "col-3 col-text-right")
    for row in table:
        match = row.find("a","table-cell-container")
        link = match.get("href")

        'cut ID from whole link'
        regex = r"https\:\/\/www\.primeleague\.gg\/de\/leagues\/matches\/(\d+).+"
        match_id = re.search(regex, link)

        match_history.append(match_id.group(1))
    return match_history


def get_champions(match_id: str):
    'returns a dictionary with summoners and champions'

    match_soup = get_soup(pl_matches + match_id)

    'extracts the summoner names'
    summoners = []
    for i in match_soup.find_all("div", "submatch-lol-player-name"):
        summoners.append(i.text.lower())

    'extracts the played champions'
    champions = []
    for i in match_soup.find_all("img", "img-player-hero"):
        champions.append(i.get("title"))

    if summoners or champions:
        'from start to half length of champions'
        game1_champions = champions[:len(champions)//2]
        'from half length to end of champions'
        game2_champions = champions[len(champions)//2:]
        game1_summoners = summoners[:len(summoners)//2]
        game2_summoners = summoners[len(summoners)//2:]

        game1 = dict(zip(game1_summoners, game1_champions))
        game2 = dict(zip(game2_summoners, game2_champions))
        
        match = {
            "game1" : game1,
            "game2" : game2
        }
        
        return match


def count_champions(team_id: str):
    'returns a dictionary of played champs and their play count'
    played_champs = []

    for match in get_matches(team_id):
        if get_champions(match):
            for summoner in list(get_champions(match)["game1"]):
                if summoner in get_summoners(team_id):
                    'only appends the summoners of one team'
                    played_champs.append(get_champions(match)["game1"][summoner])
                    
            for summoner in list(get_champions(match)["game2"]):
                if summoner in get_summoners(team_id):
                    played_champs.append(get_champions(match)["game2"][summoner])

    counted_champs = Counter(played_champs)
    sorted_counted_champs = dict(sorted(counted_champs.items(), key=lambda x: x[1], reverse=True))

    return(sorted_counted_champs)

def get_all_bans(match_id: str):
    'returns a dictionary with champions and their bancount'

    match_soup = get_soup(pl_matches + match_id)
    'extracts the banned champions'
    banned_champs = []
    for imagebox in match_soup.find_all("div", "submatch-lol-bans"):
            for image in imagebox.findAll("img"):
                banned_champs.append(image.get("title"))

    counted_bans = Counter(banned_champs)
    sorted_counted_bans = dict(sorted(counted_bans.items(), key=lambda x: x[1], reverse=True))
        
    return sorted_counted_bans

def get_bans_against(match_id: str, team_id: str):
    'returns a dictionary with champions and their bancount'

    match_soup = get_soup(pl_matches + match_id)
    'extracts the banned champions'
    banned_champs = []
    for imagebox in match_soup.find_all("div", "submatch-lol-bans"):
            for image in imagebox.findAll("img"):
                banned_champs.append(image.get("title"))

    bans = []
    blueside = started_blueside(match_id,team_id)
    for counter,ban in enumerate(banned_champs):
        if not(blueside ^ int(counter/5)%2):
            bans.append(ban)

    return bans

def started_blueside(match_id: str, team_id: str):
    match_soup = get_soup(pl_matches + match_id)
    team = get_summoners(team_id)
    if match_soup.find("div", "submatch-lol-player-name").text.lower() in team:
        return True
    return False


