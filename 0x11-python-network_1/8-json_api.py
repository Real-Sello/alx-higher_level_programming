#!/usr/bin/python3
"""
 a Python script that takes in a letter and sends a POST request to
 http://0.0.0.0:5000/search_user with the letter as a parameter
"""


import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        URL = "http://0.0.0.0:5000/search_user"
        q = ""

    values = {'q': q}
    request = requests.post(URL, data=values)
    try:
        response = request.json()
        if response:
            print("[{}] {}".format(response['id'], response['name']))
        else:
            print("No result")
    except (TypeError, ValueError):
        print("Not a valid JSON")
