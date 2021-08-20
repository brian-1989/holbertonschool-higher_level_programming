#!/usr/bin/python3
""" This script takes an URl, sends a request and
displays the value of the X-Request-Id.

"""
import urllib.request
import sys

if __name__ == "__main__":
    _url = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(_url) as response:
        for key, value in response.headers.items():
            if key == 'X-Request-Id':
                print(value)
