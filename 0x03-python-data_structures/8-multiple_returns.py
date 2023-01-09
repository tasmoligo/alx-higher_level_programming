#!/usr/bin/python3
def multiple_returns(sentence):
    my_tuple = tuple(sentence)
    if len(my_tuple) == 0:
        return len(my_tuple), None
    else:
        return len(my_tuple), my_tuple[0]
    print(my_tuple)
