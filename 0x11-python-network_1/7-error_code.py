#!/usr/bin/python3
"""prints the X-Request-Id of the url"""
from sys import argv, exit
import requests


if __name__ == "__main__":
    if len(argv) != 2:
        exit(1)
    url = argv[1]

    try:
        req = requests.get(url)
        if req.status_code == 200:
            content = req.text
            print(content)
        else:
            print(f"Error code: {req.status_code}")
    except e:
        print(e)
