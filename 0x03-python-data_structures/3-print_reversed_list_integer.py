#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    reversed_list = range(len(my_list) - 1, -1, -1)
    my_list.reverse()
    for my_num in reversed_list:
        print("{:d}".format(my_num))
