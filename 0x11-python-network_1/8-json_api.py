#!/usr/bin/python3
"""
 a Python script that takes in a letter and sends a POST request to
 http://0.0.0.0:5000/search_user with the letter as a parameter
"""


import sys
import requests

if __name__ == "__main__":
    URL = "http://0.0.0.0:5000/search_user"
    q = ""

    if len(sys.argv) > 1:
        q = sys.argv[1]
    values = {"q": q}

    request = requests.post(URL, data=values)
    try:
        response = request.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except (TypeError, ValueError):
        print("Not a valid JSON")
