#!/usr/bin/python3
""" This script takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8).

"""

import urllib.request
import sys

if __name__ == "__main__":
    _url = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(_url) as response:
            _page = response.read().decode('utf-8')
            print(_page)
    except(urllib.error.HTTPError) as _error:
        print("Error code: {}".format(_error.code))
