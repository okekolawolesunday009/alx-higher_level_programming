#!/usr/bin/python3
"""gets the user_id frim github api"""
import requests
from requests import auth
from requests.auth import HTTPBasicAuth
from sys import argv, exit


if __name__ == "__main__":
    if len(argv) != 3:
        exit(1)
    username = argv[1]
    password = argv[2]
    api_url = "https://api.github.com/user" 
    r = requests.get(api_url, auth=auth.HTTPBasicAuth(username, password))
    user_data = r.json()
    print(user_data.get('id'))
