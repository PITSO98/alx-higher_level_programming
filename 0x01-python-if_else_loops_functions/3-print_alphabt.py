#!/usr/bin/python3
for c in range(ord('a'), ord('z') + 1):
    if not c == (ord('e') and  ord('q')):
        print("{:c}".format(c), end="")
