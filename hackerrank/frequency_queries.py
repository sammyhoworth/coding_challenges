# challenge can be found here: https://www.hackerrank.com/challenges/frequency-queries/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):
    res = []
    freqs = {}
    vals = {}
    for q in queries:
        if q[0] == 1:
            # if number already exists in freq, decrease count of its value in vals by 1
            if q[1] in freqs:
                vals[freqs[q[1]]] -= 1
            # update frequency for specific number
            freqs[q[1]] = freqs.get(q[1], 0) + 1
            # update value for specific count (+1)
            vals[freqs[q[1]]] = vals.get(freqs[q[1]],0) + 1


        elif q[0] == 2:
            # if number already exists in freq ...
            if q[1] in freqs:
                # ... decrease value in vals by 1 (dont let it drop below 0)
                if vals[freqs[q[1]]] > 0:
                    vals[freqs[q[1]]] -= 1
                # ... decrease count by 1
                if freqs[q[1]] > 0:
                    freqs[q[1]] -= 1
                # ... increase vals value for new value
                vals[freqs[q[1]]] = vals.get(freqs[q[1]],0) + 1

        elif q[0] == 3:
            res.append(min(1, vals.get(q[1], 0)))
        
    return res




if __name__ == '__main__':
    fptr = open("./outputs/output_frequency_queries.txt", "w+") 

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
