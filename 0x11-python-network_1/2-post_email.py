#!/usr/bin/python3
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from urllib.parse import urlencode
from sys import argv, exit


if __name__ == "__main__":
        if len(argv) != 3:
            exit(1)
        url = str(argv[1])
        email = argv[2]

        data = urlencode({'email': email}).encode('utf-8')
        req = Request(url, data=data, method='POST')

        try:
            with urlopen(req) as response:
                content = response.read()
                uf8_content = content.decode('utf-8')

            print("Your email is:", email)
            print(content)
        except URLError as e:
            print(e.reason)


