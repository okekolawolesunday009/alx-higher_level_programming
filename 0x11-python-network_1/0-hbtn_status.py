#!/usr/bin/python3
"Fecthes data from the url"
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError


if __name__ == "__main__":
    url = ' https://alx-intranet.hbtn.io/status'
    req = Request(url)
    with urlopen(req) as response:
        content = response.read()
        utf8_content = content.decode('utf-8')
        print("Body response:")
        print("    - type:", type(content))
        print("    - content:", repr(content))
        print("    - utf8 content:", utf8_content)

    except urllib.error.URLError as e:
        print(e.reason)
