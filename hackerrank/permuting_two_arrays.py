#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoArrays function below.
def twoArrays(k, A, B):
    sA = sorted(A)
    sB = sorted(B)[::-1]
    for i in range(len(sA)):
        if sA[i] + sB[i] < k:
            return "NO"
    return "YES"

def twoArrays_b(k, a, b):
    # similar to above, but condensed and uses zip() and reverse parameter in sorted() function
    if all(sum(pair) >= k for pair in zip(sorted(a), sorted(b, reverse=True))):
        return "YES"
    else:
        return "NO"
    

if __name__ == '__main__':
    fptr = open("./outputs/permuting_two_arrays.txt", "w+") 

    q = int(input())

    for q_itr in range(q):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        A = list(map(int, input().rstrip().split()))

        B = list(map(int, input().rstrip().split()))

        result = twoArrays_b(k, A, B)

        fptr.write(result + '\n')

    fptr.close()
