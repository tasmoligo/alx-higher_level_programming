#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return (None)
    elif idx >= len(my_list):
        return (None)
    else:
        for x in my_list:
            if x == my_list[idx]:
                return (x)
