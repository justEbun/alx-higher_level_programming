#!/usr/bin/python3
import string
alphabet = string.ascii_lowercase
for letter in alphabet:
    if (letter == "q") or (letter == "e"):
        continue
    print("{}".format(letter), end="")
