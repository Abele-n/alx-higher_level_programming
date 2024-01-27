#!/usr/bin/python3
"""
script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
from sys import argv


if __name__ == '__main__':
    url = "http://0.0.0.0:5000/search_user"
    info = {"q": argv[1][0] if len(argv) > 1 else ""}
    response = requests.post(url, data=info)
    try:
        n = response.json()
        if not n:
            print("No result")
        else:
            print("[{}] {}".format(n.get("id"), d.get("name")))
    except ValueError:
        print("Not a valid JSON")
