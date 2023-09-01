#!/usr/bin/python3
"""
a Python script that fetches https://alx-intranet.hbtn.io/status:

    -We use the package urllib
    -We are not allowed to import any packages other than urllib
    -The body of the response must be displayed like the following example
        (tabulation before -)
    -We use a with statement
"""


import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    status = response.read()
    print("Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: \
{}".format(type(status), status, status.decode('utf-8')))
