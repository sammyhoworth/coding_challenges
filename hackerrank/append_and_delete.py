#!/bin/python3

import math
import os
import random
import re
import sys



# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):

    # get rid of easy cases
    #   t is too long (or, s is too short)
    if len(t) > len(s)+k:
        return "No"

    if len(s) + len(t) <= k:
        # can delete all of s and create all of t
        return "Yes"

    e = 0
    while (s[e] == t[e]) and (e < len(s)-1) and (e < len(t)-1):
        e += 1    
    # now working with relevant portion of s and t (call them s2 and t2)
    s2 = s[e:]
    t2 = t[e:]

    # must be able to delete all of s2 and add all of t2 with number of moves remaining
    req_moves = len(s2) + len(t2)
    #       of course it's possible to reduce this to a couple if-else checks but leaving it as is for ease of understanding
    if req_moves == k:
        return "Yes"
    elif req_moves > k:
        return "No"
    elif req_moves < k:
        if (req_moves - k) % 2 == 0:
            # can repeatedly add and delete any letter
            return "Yes"
    return "No"


if __name__ == '__main__':
    fptr = open("./outputs/append_and_delete.txt", "w+") 

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
