# problem available here: https://www.hackerrank.com/challenges/sparse-arrays/problem

import math
import os
import random
import re
import sys

# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    counts = dict()
    for i in strings:
        counts[i] = counts.get(i, 0)+1
    
    output_queries = [counts.get(qq,0) for qq in queries]
    return output_queries



if __name__ == '__main__':

    fptr = open("./outputs/output_sparse_arrays.txt", "w+") 

    #strings_count = int(input())

    inputs = []

    with open("./inputs//input_sparse_arrays.txt", "r") as opfile:
        for line in opfile:
            inputs.append(line.strip())

    strings = inputs[1:int(inputs[0])+1]
    queries =  inputs[int(inputs[0])+2:]
    print(strings)
    print(queries)
    
    result = matchingStrings(strings, queries)
    print(result)
    fptr.write(str(result) + '\n')
    fptr.close()