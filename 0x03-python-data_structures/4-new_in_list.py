#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
     """ replaces an element in a list at a specific position without modifying the original list"""
     if idx >= 0 and idx < len(my_list):
         my_list[idx] = element
         return my_list
     else:
          return None