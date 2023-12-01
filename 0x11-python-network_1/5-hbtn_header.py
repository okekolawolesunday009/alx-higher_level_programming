#!/usr/bin/python3
"""prints the X-Request-Id of the url"""
from sys import argv, exit
import requests


if __name__ == "__main__":
    if len(argv) != 2:
        exit(1)
    url = argv[1]
    req = requests.get(url)
    if req.status_code == 200:
        ri = req.headers.get('X-Request-Id')
        if ri:
            print(ri)
        else:
            print("x-Request-Id not found")
    else:
        print(f"Error:{req.status_code}")
