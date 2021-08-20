#!/usr/bin/python3
""" This script takes an URL, send a POST request to the passed URL
with the email as a parameter.

"""
from urllib import request, parse
import sys

if __name__ == "__main__":
    data = {}
    data['email'] = sys.argv[2]
    values_url = parse.urlencode(data)
    values_url = values_url.encode('ascii')
    full_url = request.Request(sys.argv[1], values_url)
    with request.urlopen(full_url) as response:
        print(response.read().decode())
