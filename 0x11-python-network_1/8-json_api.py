#!/usr/bin/python3
""" This script takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.

"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        myobj = {"q": sys.argv[1]}
    else:
        myobj = {"q": ""}
    r = requests.post('http://0.0.0.0:5000/search_user', data=myobj)
    try:
        if len(r.json()) > 0:
            print("[{}] {}".format(r.json()['id'], r.json()['name']))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
