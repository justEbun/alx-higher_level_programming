#!/usr/bin/python3

def print_last_digit(number):
    number = list(str(number))
    i = number[len(number) - 1]
    i = int(i)
    print(i)
