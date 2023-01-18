#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best_score = ''
    num = 0
    for key, value in a_dictionary.items():
        if value > num:
            num = value
            best_score = key
    return best_score
