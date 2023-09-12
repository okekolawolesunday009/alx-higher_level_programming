#!/usr/bin/python3

import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "my_list.json"

if __name__ == "__main__":
    try:
        lists = load_from_json_file(filename)
    except:
        lists = []
    for av in sys.argv[1:]:
        lists.append(av)
    save_to_json_file(lists, filename)
