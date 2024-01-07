#!/usr/bin/python3
def multiple_returns(sentence):
    lenght = len(sentence)
    if lenght == 0:
        first_char = None
        _tuple = (lenght, first_char)
        return _tuple
    else:
        first_char = sentence[0]
        _tuple = (lenght, first_char)
        return _tuple
