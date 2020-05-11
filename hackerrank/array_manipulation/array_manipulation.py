# See 'hard' problem here:    https://www.hackerrank.com/challenges/crush/problem
# Note that the solution is the function, arrayManipulation, and that I have edited the rest of the code to function well locally (feed in a text file of operations)

import math
import os
import random
import re
import sys


def arrayManipulation( n, queries):
    arr = [0 for x in range(n)]
    
    for q in queries:
        arr[q[0] - 1] += q[2]
        if not q[1] == len(arr):
            # personal hold up was here (other than the obvious program complexity hurdle -- the reason this challenge is 'hard' difficulty) 
            # as I either:
            #   (1) ran into an error where q[1] ('b' in the challenge description) does not exist due to Python's list indexing, or
            #   (2) handled it by using an array with an additional element on the end, but then the subtraction doesn't do anything
            arr[q[1]] -= q[2]

    mx = 0
    s = 0

    for i in arr:
        s += i
        mx = max(mx,s)

    return mx



if __name__ == '__main__':
    
    fptr = open("./hackerrank/array_manipulation/output.txt", "w+") 

    operations = []

    with open("./hackerrank/array_manipulation/operations.txt", "r") as opfile:
        # replace with 'testcase_4.txt' for a more challenging case involving an array of length 4000 and 30,000 operations
        # note that testcase_4.txt is from hackerrank's evaluation testcases (need points to 'purchase'), so the version included here has been slightly edited
        for line in opfile:
            operations.append(line.strip())

    nm = operations[0].split()
    n = int(nm[0])
    m = int(nm[1])
    
    queries = []
    for ln in operations[1:]:
        queries.append(list(map(int, ln.split())))
    
result = arrayManipulation(n, queries)
print(result)
fptr.write(str(result) + '\n')

fptr.close()
