#!/usr/bin/python3
"""prints the JSON of the url"""
from sys import argv, exit
import requests


if __name__ == "__main__":
    if len(argv) == 2:
        data = {'q': argv[1]}
    else:
        data = {}
    url = 'http://0.0.0.0:5000/search_user'
    req = requests.post(url, data=data)
    type_res = req.headers['content-type'] = 'application/json'

    if type_res:
        res = req.json()
        _id = res.get('id')
        name = res.get('name')
        if res != {} and _id and name:
            print("[{}] {}".foramt(_id, name))
        else:
            print('No result')
    else:
        print('Not a valid JSON')
