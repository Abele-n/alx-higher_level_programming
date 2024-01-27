#!/usr/bin/python3
"""
script that takes 2 arguments in order to solve this challenge.
The first argument will be the repository name
The second argument will be the owner name
"""
import requests
from sys import argv


if __name__ == '__main__':
    r = requests.get("http://api.github.com/repos/{}/{}/commits"
                     .format(argv[2], argv[1]))
    commits = r.json()
    for commit in commits[:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
