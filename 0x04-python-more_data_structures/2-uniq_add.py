#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique_list = set(my_list)
    my_num = 0

    for x in unique_list:
        my_num += x
    return my_num
