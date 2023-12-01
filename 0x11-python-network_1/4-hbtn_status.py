#!/usr/bin/python3
import requests

if __name__ == "__main__":
        url = ' https://alx-intranet.hbtn.io/status'
        req = requests.get(url)
        content = req.text
        print("Body response:")
        print("    - type:", type(content))
        print("    - content:", (content))
