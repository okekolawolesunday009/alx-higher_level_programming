#!/usr/bin/python3


def append_write(filename="", text=""):
    try:
        with open(filename, "a", encoding='utf-8') as file:
            lines = file.write(text)
            return (lines)
    except FileNotFoundError:
        print(f"No such file or directory")
        return None
