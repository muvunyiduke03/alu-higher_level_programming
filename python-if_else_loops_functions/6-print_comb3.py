#!/usr/bin/python3
for i in range(100):
    for j in range(i + 1, 100):
        if i != j:
            print("{:02d}{:02d}".format(i, j), end=", " if i < 98 or j < 99 else "\n")
