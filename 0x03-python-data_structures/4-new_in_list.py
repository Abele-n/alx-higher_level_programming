#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    original_copy = [m for m in my_list]
    original_copy[idx] = element
    return original_copy
