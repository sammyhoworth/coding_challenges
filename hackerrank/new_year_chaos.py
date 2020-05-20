# Problem available here: https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
# uncomment print statements for debugging


import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    # a person can only bribe the person in front of them (and jump them in line)
    # a person can at most bribe two people
    # line starts as 1 2 3 4 ... etc.
    nmoves = 0
    
    for i in range(len(q)):
        if q[i] - (i+1) >= 3:
            # if q[i] is 3 or greater than i+1 (its 'natural' value), then it must've jumped at least 3 times to get there
            print ("Too chaotic")
            return
        for j in range(max(0,q[i]-2),i):
            #print("    checking {} against {}".format(q[j], q[i]))
            if q[j] > q[i]:
                nmoves += 1
                #print("       nmoves += 1:", nmoves)

    print(nmoves)
    return 



if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
        
