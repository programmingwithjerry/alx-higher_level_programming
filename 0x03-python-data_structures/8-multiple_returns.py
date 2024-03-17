#!/usr/bin/python3

def multiple_returns(sentence):
    length_of_sentence = len(sentence)
    if length_of_sentence == 0:
        tuple_of_empty = (0, None)
        return tuple_of_empty
    else:
        result = (length_of_sentence, sentence[0:1])
        return result
