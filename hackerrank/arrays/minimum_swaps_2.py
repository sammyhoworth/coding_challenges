#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    a = arr

    i = 0
    nmoves = 0
    while i < len(a):
        print("i", i)
        if a[i] - 1 == i:
            print("     a[i]-1 == i")
            i += 1
        else:
            # if a[i] is not in its right spot, switch it with whatever is
            t1 = a[i]
            t2 = a[t1-1]
            a[i] = t2
            a[t1-1] = t1
            nmoves += 1
    return nmoves
            


if __name__ == '__main__':
    
    fptr = open("./outputs/output_minimum_swaps_2.txt", "w+") 

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
