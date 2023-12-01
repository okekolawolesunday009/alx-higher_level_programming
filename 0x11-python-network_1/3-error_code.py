#!/usr/bin/python3
"""print error code"""
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from urllib.parse import urlencode
from sys import argv, exit


if __name__ == "__main__":
    if len(argv) != 2:
        exit(1)
    url = argv[1]
    req = Request(url)
    try:
        with urlopen(req) as response:
            content = response.read()
            uf8_content = content.decode('utf-8')
            print(ut8_content)
    except HTTPError as e:
        print(f"Error code: {e.code}")
