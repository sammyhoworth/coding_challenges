#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):
    sorted_prices = sorted(prices)
    ntoys = 0

    while k > 0:
        k -= prices[i]
        ntoys += 1
    return ntoys - 1





if __name__ == '__main__':
    fptr = open("./outputs/output_mark_and_toys.txt", "w+") 

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
