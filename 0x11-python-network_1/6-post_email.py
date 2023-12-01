#!/usr/bin/python3
"""prints the X-Request-Id of the url"""
from sys import argv, exit
import requests


if __name__ == "__main__":
    if len(argv) != 3:
        exit(1)
    url = argv[1]
    email = argv[2]
    data = {'email': email}

    try:
        req = requests.post(url, data=data)
        if req.status_code == 200:
            content = req.text
            print(content)
        else:
            print(f"Error: {response.status_code}")
    except e:
        print(e)
