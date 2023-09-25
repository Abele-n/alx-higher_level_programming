#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """x elements of a list are printed
    Args:   
        my_list: list from where the elements are printed
        x: number of my_list elements to print
    Returns:
        the number of elements printed
    """

    naf = 0
    for j in range(x):
        try:
            print("{}".format(my_list[m]), end = "")
            naf += 1
        except IndexError:
            break
        print("")
        return(naf)
