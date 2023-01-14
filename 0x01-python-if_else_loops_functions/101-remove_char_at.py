#!/usr/bin/python3

def remove_char_at(str, n):
    str = list(str)
    str.pop(n)
    result = ""
    for letter in str:
        result += letter
    return result
