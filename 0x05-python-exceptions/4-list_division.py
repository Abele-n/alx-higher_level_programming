#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    my_new_list = []
    for j in range(0, list_length):
        try:
            my_div = my_list_1[j] / my_list_2[j]
        except TypeError:
            print("wrong type")
            my_div = 0
        except ZeroDivisionError:
            print("division by 0")
            my_div = 0
        except IndexError:
            print("out of range")
            my_div = 0
        finally:
            my_new_list.append(my_div)
            return (my_new_list)
