# challenge available here: https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem

'''
The strategy employed here loops through a string, obtaining all substrings of lenth 1, then all of length 2, etc.

For each defined substring length, count how many times each sorted value has already occurred.
Sorting is used as an efficient way to check if anagram exists, as a string is an anagram of another string if they are identical once sorted
'''

#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    # traverse the string for all sets of consecutive elements of same length

    lens = len(s)
    nanagrams = 0

    for i in range(1, lens):
        counts = {} # this dictionary is used to count all instances of sorted strings of length i. Gets re-initated as empty upon moving to the next length

        for j in range(lens - i + 1): # (lens - i) handles cases when looking at substrings of length > 1
            # obtain substring of desired length beginning at j
            ts = s[j : j+i]
            ts = ''.join(sorted(ts)) # alphabetize it for quicker anagram check

            # check if temp string (ts) was already found. If so, add 1 to its value, otherwise insert it with value 1
            counts[ts] = counts.get(ts, 0) + 1

            # an anagram exists if the count is greater than 1
            nanagrams += counts[ts] - 1
            
    return nanagrams


if __name__ == '__main__':
    fptr = open("./outputs/output_sherlock_and_anagrams.txt", "w+") 

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)
        print(result)
        fptr.write(str(result) + '\n')

    fptr.close()
