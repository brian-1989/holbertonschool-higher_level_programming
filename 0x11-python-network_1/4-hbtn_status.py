#!/usr/bin/python3
""" This script that fetches url: https://intranet.hbtn.io/status.

"""

import requests

if __name__ == "__main__":
    response = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}\n\t- content: {}".format(
        type(str(response.__class__)), response.content.decode('utf-8')))
