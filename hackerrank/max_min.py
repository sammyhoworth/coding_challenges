#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxMin function below.
def maxMin(k, arr):
    sarr = sorted(arr)

    cmaxMin = sarr[k-1] - sarr[0]
    for i in range(k-1, len(sarr)):
        cmaxMin = min(cmaxMin, sarr[i] - sarr[i-k+1])
    
    return cmaxMin





if __name__ == '__main__':
    fptr = open("./outputs/output_max_min.txt", "w+") 

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
