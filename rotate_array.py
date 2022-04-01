#!/usr/bin/env/ python3


list = [1,2,3,4,5]
k = 6
newlist = []
def rotate_array():
    p = None
    for i in range(len(list)):
        if p == None:
            p = len(list)-k 
        newlist.append(list[p])
        p  = (p+1)%len(list)
    print(newlist)
rotate_array()
