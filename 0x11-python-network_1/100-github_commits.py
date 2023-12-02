#!/usr/bin/python3
import requests
from requests import auth
from requests.auth import HTTPBasicAuth
from sys import argv, exit


if __name__ == "__main__":
    if len(argv) != 3:
        exit(1)
    owner = argv[1]
    repo = argv[2]
    i = 9
    api_url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    r = requests.get(api_url)
    json_data = r.json()
    for i, element in enumerate(json_data[:i]):
        sha = element.get('sha')
        author = element.get('commit').get('author').get('name')
        print(f"{sha}: {author}")
