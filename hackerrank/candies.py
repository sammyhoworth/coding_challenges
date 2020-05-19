# problem available here: https://www.hackerrank.com/challenges/candies/problem
'''
This solution takes too long to run for 1 out of the 18 test cases. 
An improved solution to follow at a later date. Likely one that tries to run once from left to right then again from right to left,
rather than this approach of moving left and right several times as it traverses the original array from left to right
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the candies function below.
def candies(n, arr):
    # start by looking at the second child. If lower than the first child, give first child a 2, otherwise give first child a 1, and continue normally
    candies = [1]*n
    
    if arr[0] > arr[1]:
        candies[0] += 1

    i = 1
    while i < len(arr):
        if arr[i] > arr[i-1]:
            if not (candies[i] > candies[i-1]):
                candies[i] = candies[i-1] + 1
            i += 1
            
            
        elif arr[i] < arr[i-1]:
            if not (candies[i] < candies[i-1]):
                candies[i-1] = candies[i] + 1
                i -= 1
            else:
                i += 1
                
        else:
            i+=1
    return sum(candies)





if __name__ == '__main__':
    fptr = open("./outputs/output_candies.txt", "w+") 

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
