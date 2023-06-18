#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def s(x):
        return (x if x != search else replace)
    return list(map(s, my_list))
