#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def getSubstrings(s):
    substrings = []
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            substrings.append(s[i:j])
    #print("SUBSTRINGS")
    #print("        ", substrings)
    return substrings


def is_anagram(s1, s2):
    # returns 1 if the two substrings are anagrams
    # else returns 0
    if len(s1) != len(s2):
        return 0
    
    x1 = ''.join(sorted(s1))
    x2 = ''.join(sorted(s2))
    for y in range(len(x1)):
        if x1[y] != x2[y]:
            return 0
    return 1
    '''
    check = {}

    for x in s1:
        check[x] = check.get(x, 0) + 1
    for x in s2:
        if x in check:
            check[x] = check.get(x,0) - 1
        else:
            return 0
    
    for v in check.values():
        if v != 0:
            return 0
    return 1
    '''




# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    # for all pairs of substrings, count the number of anagrams
    n_anagrams = 0
    ss = getSubstrings(s)

    for i in range(len(ss)):
        for j in range(i, len(ss)):
            if i != j:
                if len(ss[i]) == len(ss[j]):
                #print("ADDING {} to n_anagrams".format(int(is_anagram(ss[i], ss[j]))))
                    n_anagrams += is_anagram(ss[i], ss[j])


    print(n_anagrams)
    return n_anagrams

if __name__ == '__main__':
    fptr = open("./outputs/output_sherlock_and_anagrams.txt", "w+") 

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
