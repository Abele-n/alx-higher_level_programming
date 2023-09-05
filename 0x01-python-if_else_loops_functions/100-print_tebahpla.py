#!/usr/bin/python3
x = 0
for m in range(ord('z'), 96, -1):
    print("{}".format(chr(m - x)), end="")
    x = 0 if x == 0 else 0
