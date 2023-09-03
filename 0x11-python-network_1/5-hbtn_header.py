#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a request to the URL
and displays the value of the variable X-Request-Id in the response header
"""


import sys
import requests

if __name__ == '__main__':
    req_get = requests.get(sys.argv[1])
    print("{}".format(req_get.headers.get('X-Request-Id')))
