#!/usr/bin/python3
def islower(c):
    """Check for lowercase characters."""
    if ord(c) >= 9:
        return True
    elif ord(c) <= 122:
        return False
