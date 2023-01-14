#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

print(f"Last digit of {number}", end="")
number = list(str(number))
i = number[len(number) - 1]
i = int(i)
if '-' in number:
    i = -i

if i > 5:
    text = "and is greater than 5"
elif i == 0:
    text = "and is 0"
elif (i < 6) and (i != 0):
    text = "and is less than 6 and not 0"

print(f" is {i} {text}")
