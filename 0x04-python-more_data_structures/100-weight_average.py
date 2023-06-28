#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        average = 0
        denom = 0
        total = 0
        for i in my_list:
            denom += i[1]
            total += i[0] * i[1]
        return total/denom
    else:
        return 0
