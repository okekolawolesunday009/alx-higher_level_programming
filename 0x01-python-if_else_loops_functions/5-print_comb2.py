#!/usr/bin/python3
for tens in range(10):
    for units in range(10):
        if tens != 8 and units != 9:
            print("{:01}{:01}".format(tens, units), end=", ")
        else:
            print("{:01}{:01}".format(tens, units), end=" ")
       
     