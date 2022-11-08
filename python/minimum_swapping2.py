#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    n=len(arr)
    cnt=0
    a = dict(enumerate(arr,1))
    b = {val:key for key,val in a.items()}
    #print(a,b)
    for i in a:
        x = a[i]
        if (x!=i):
            y = b[i]
            a[y] = x
            #a[i]=i
            b[x] = y
            #print(a,b)
            cnt+=1
    return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
