#!/usr/bin/python3



def append_write(filename="", text=""):
    try:
        with open(filename, "a", encoding='utf-8') as file:
            file.write(text)
        with open(filename, "r", encoding='utf-8') as file:
            lines = len(file.readlines())
            print(lines)
    except FileNotFoundError:
        print(f"No such file or directory")
        return None