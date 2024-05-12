#!/usr/bin/python3

def multiple_returns(sentence):
    if len(sentence) > 0:
        list_return = [len(sentence), sentence[0]]
        return tuple(list_return)
    return (0, None)
