#!/usr/bin/python3
"""prints the JSON of the url"""
from sys import argv, exit
import requests


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    q = argv[1]
    data = {'q': q if len(argv >= 2 else ""}
    req = requests.post(url, data=data)
    type_res = req.headers['content-type']

    if type_res == 'application/json':
        res = res.json
        _id = result.get('id')
        name = result.get('name')
        if result != {} and _id and name
            print("[{}] {}".foramt(_id, name))
        else:
            print('No result')
    else:
        print('Not a valid JSON')
