#!/usr/bin/python3
for n in range(0, 10):
    for j in range(n + 1, 10):
        if n != 8 or j != 9:
            if n != 0 or j != 1:
                print(", ", end='')
            print("{:02}".format(n * 10 + j), end='')

print()
