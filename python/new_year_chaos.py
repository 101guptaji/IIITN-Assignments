'''It's New Year's Day and everyone's in line for the Wonderland rollercoaster ride! There are a number of people queued up, and each person wears a sticker indicating their initial position in the queue. Initial positions increment by from at the front of the line to
 'n' at the back. 
Any person in the queue can bribe the person directly in front of them to swap positions. If two people swap positions, they still wear the same sticker denoting their original places in line. One person can bribe at most two others. For example, if n=8 and Person5 and Person 4,
bribes, the queue will look like this: 1 2 3 5 4 6 7 8.
Fascinated by this chaotic queue, you decide you must know the minimum number of bribes that took place to get the queue into its current state!
'''

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    n=len(q)
    ans=0
    for i in range(n-1,-1,-1):
        if(q[i]-(i+1)>2):
            print("Too Chaotic")
            return
        for j in range(max(0,q[i]-2),i):
            if(q[j]>q[i]): ans+=1
    print(ans)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
