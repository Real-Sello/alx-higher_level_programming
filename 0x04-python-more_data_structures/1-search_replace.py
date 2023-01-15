#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """
    Replace all occurrences of an element by another in a new list.
    """
    update_list = my_list[:]
    for elem in range(len(update_list)):
        if update_list[elem] == search:
            update_list[elem] = replace
    return (update_list)
