#!/usr/bin/python3
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from sys import argv, exit


if __name__ == "__main__":
    if len(argv) != 2:
        exit(1)
    url = argv[1]
    try:
        with urlopen(url) as response:
            content = response.read()
            utf8_content = content.decode('utf-8')
            request_id = response.getheader('X-Request-Id')
        print(request_id)
    except HTTPError as e:
        print(e.reason)