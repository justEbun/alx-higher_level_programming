#!/usr/bin/python3
combinations = set()

for i in range(10):
    for j in range(10):
        if i != j and (i, j) not in combinations and (j, i) not in combinations:
            if (i < 8) or (j < 9):
                print("{}{}, ".format(i,j), end="")
            else:
                print("{}{}".format(i,j))
            combinations.add((i,j))
