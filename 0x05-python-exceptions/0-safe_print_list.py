#!/usr/bin/python3
"""P"""
def safe_print_list(my_list=[], x=0):
    c = 0
    for i in range( x):
        try:
            print("{}".format(my_list[i]), end="")
            c += 1
        except:
            break
    print("")
    return (c)
