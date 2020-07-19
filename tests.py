#!/bin/python3

from main import Team

eko = Team(id)

soup = eko.get_matches()

for e in soup.find_all('a'):
    print(e.get('href'))