#!/usr/bin/python3
def multiple_returns(sentence):
    length = 0
    character = None
    if len(sentence) == 0:
        return (length, character)
    else:
        return (len(sentence), sentence[0])
