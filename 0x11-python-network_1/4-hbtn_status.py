#!/usr/bin/python3
"""
a Python script that fetches https://alx-intranet.hbtn.io/status
"""


import requests
if __name__ == "__main__":
    URL = "https://alx-intranet.hbtn.io/status"
    request = requests.get(URL)
    print("Body response:\n\t- type: {}\n\t- content: {}"
          .format(type(request.text), request.text))
