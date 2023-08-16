#!/usr/bin/python3
def new_in_list(my_list, idx, element):
     """ replaces an element in a list at a specific position without modifying the original list"""
     if idx >= 0 and idx < len(my_list):
         new_list = my_list[:]
         new_list[idx] = element
         return new_list
     else:
          return None


if __name__ == "__main__":
    new_in_list()
