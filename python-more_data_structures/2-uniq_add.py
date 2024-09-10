#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Use a set to ensure all values are unique, then sum the set
    return sum(set(my_list))
