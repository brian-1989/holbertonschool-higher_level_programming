#!/usr/bin/python3
def multiple_returns(sentence):
    i = 0
    if sentence == "":
        tuple_total = len(sentence), None
        return tuple_total
    else:
        tuple_total = len(sentence), sentence[i]
        return tuple_total
