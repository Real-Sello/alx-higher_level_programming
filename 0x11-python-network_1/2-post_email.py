#!/usr/bin/python3
"""
a Python script that takes in a URL and an email, 
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)

    -The email must be sent in the email variable
    -We use the packages urllib and sys
    -We do not to import packages other than urllib and sys
    -No need to check arguments passed to the script (number or type)
    -We use the with statement
"""


import sys
import urllib.request
import urllib.parse

if __name__ == '__main__':
    URL = sys.argv[1]
    email = sys.argv[2]
    value = {"email": email}
    data = urllib.parse.urlencode(value)
    data = data.encode('utf-8')
    request = urllib.request.Request(URL, data)

    with urllib.request.urlopen(request) as response:
        print("{}".format(response.read().decode('utf-8')))
