#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_sum = 0
    for i in set(my_list):
        my_sum += i
    return my_sum
