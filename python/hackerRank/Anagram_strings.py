#Sherlock and Anagrams
'''Two strings are anagrams of each other if the letters of one string can be rearranged to form the other string. Given a string, find the number of pairs of substrings of the string that are anagrams of each other.

For example s = mom, the list of all anagrammatic pairs is [m, m], [mo, om] at positions [[0], [2]], [[0, 1], [1, 2]] respectively.'''

import math
import os
import random
import re
import sys

def subarray(s):
    sub=[]
    n=len(s)
    for i in range(n):
        for j in range(i+1,n+1):
            sub.append(''.join(sorted(s[i:j])))
    return sub

def isAnagram(s1,s2):
    charD={}
    for i in s1:
        charD[i]=charD.get(i,0)+1
    
    for j in s2:
        if(j in charD.keys() and charD[j]>0):
            charD[j]-=1
        else:
            return False
    #print(charD)
    return True
# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    sub=subarray(s)
    print(sub)
    n=len(sub)
    count=0
    #print(anagram('abab','abba'))
    for i in range(len(sub)):
        s1=sub[i]
        for j in range(i+1,n):
            s2=sub[j]
            #print(s1,s2)
            if((len(s1)==len(s2)) and (isAnagram(s1,s2)==True)):
                count+=1
            #print(count)
    return count
if __name__ == '__main__':
   
    s = 'abcd' #input()

    result = sherlockAndAnagrams(s)

    print(str(result) + '\n')


