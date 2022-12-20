#!/usr/bin/python3
import string
alphabet = string.ascii_lowercase
i = 0
while True:
    print("{}".format(alphabet[i]), end="")
    i += 1
    if i == len(alphabet):
        break
