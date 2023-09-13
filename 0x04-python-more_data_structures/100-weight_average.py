#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    denom = 0
    numer = 0

    for my_tupple in my_list:
        numen += my_tupple[0] * my_tupple[1]
        denom += my_tupple[1]
        
    weighted_aver = num/den
    return weighted_aver
