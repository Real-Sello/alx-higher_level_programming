#!/usr/bin/python3
"""
 a Python script that takes in a URL, sends a request to the URL and displays
 the value of the X-Request-Id variable found in the header of the response.

    -We use the packages urllib and sys
    -We do not import packages other than urllib and sys
    -The value of this variable is different for each request
    -No need to check arguments passed to the script (number or type)
    -We use a with statement
"""


import sys
import urllib.request

if __name__ == '__main__':
    with urllib.request.urlopen(sys.argv[1]) as response:
        print("{}".format(response.getheader('X-Request-Id')))
