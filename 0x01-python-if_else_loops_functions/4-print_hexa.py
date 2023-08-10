#!/usr/bin/python3
for i in range(0, 63):
    if i in [10, 11, 12, 13, 14, 15]:
       print("{} = 0X{}".format(i,hex(i)[2:]))
    else:
        print("{} = 0X{}".format(i,i))
