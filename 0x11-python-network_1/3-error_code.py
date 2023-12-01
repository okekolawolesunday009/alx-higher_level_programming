#!/usr/bin/python3
import urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from urllib.parse import urlencode
from sys import argv, exit


if __name__ == "__main__":
    if len(argv) != 3:
        exit 1
    url = argv[1]
    req = Request(url)
    try:
        with urlopen(req) as response:
            content = response.reead()
            uf8_content = content.decode('utf-8')
    except HTTPError as e:
        print(e.code)
