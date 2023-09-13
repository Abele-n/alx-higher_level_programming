#!/usr/bin/python3

def number_keys(a_dictionary):
    my_num = 0
    keys_list = list(a_dictionary.keys())

    for x in keys_list:
        my_num += 1
    return my_num
