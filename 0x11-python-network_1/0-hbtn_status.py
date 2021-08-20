#!/usr/bin/python3
""" This script that fetches url: https://intranet.hbtn.io/status.

"""
import urllib.request

if __name__ == "__main__":
    _url = urllib.request.Request('https://intranet.hbtn.io/status', )
    with urllib.request.urlopen(_url) as response:
        _page = response.read()
        print("Body response")
        print("\t- type: {}\n\t- content: {}\n\t- utf8 content: {}".format(
            type(response.read()), _page, _page.decode('utf8')))
