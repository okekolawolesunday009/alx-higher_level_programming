#!/usr/bin/python3                                                  
# prrogarm that prints capital letter                               
def uppercase(str):                                                 
    for u in str:                                                   
        if ord(u) >= 97 and ord(u) <= 122:                          
             u = chr(ord(u) - 32) 
                                            
        print("{}".format(u), end="")
    print("")
