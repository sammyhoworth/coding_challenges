#!/bin/python3

# problem available at: https://www.hackerrank.com/challenges/max-array-sum/problem
'''
Comments
- Largest hang-up for me (frustratingly so) was in the line,    maxes = [arr[0], max(arr[0], arr[1])]. I previously had it as   maxes = [arr[0], arr[1]]
- Small hurdle was allowing for the max value at a given i to simply be arr[i]
- len(arr) < 3 is simply for catching cases of a short array being passed in. This function is more efficient than checking   if i == 1    and if i == 2 repeatedly in the for loop
'''

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):

    if len(arr) < 3:
        return max(arr)

    maxes = [arr[0], max(arr[0], arr[1])]
    for i in range(2, len(arr)):        
        maxes.append(max(arr[i], maxes[i-1], maxes[i-2]+arr[i]))

    return maxes[-1]

        

if __name__ == '__main__':
    fptr = open("./outputs/output_max_array_sum.txt", "w+") 

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
