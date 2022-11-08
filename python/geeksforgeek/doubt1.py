'''Given three strings A, B and C your task is to complete the function isInterleave which returns true if C is an interleaving of A and B else returns false. C is said to be interleaving A and B, if it contains all characters of A and B and order of all characters in individual strings is preserved.

Input:
The first line of input contains an input T denoting the no of test cases. Then T test cases follow. Each test case contains three space separated strings A, B, C.

Output:
For each test case output will be 1 if C is interleaving of string A and B else 0.

Constraints:
1<=T<=100
1<=length of A, B, C <=100

Example(To be used only for expected output):
Input:
1
aab axy aaxaby

Output
1

'''
def check(A, B, C, k, i, j):
    if(k==len(C)):
        return True
    if(i==len(A) and j==len(B)):
        return True
    flag=False
    if(i<len(A) and C[k]==A[i]):
        flag=check(A, B, C, k+1, i+1, j)
    if(flag):
        return True
    if(j<len(B) and C[k]==B[j]):
        flag=check(A, B, C, k+1, i, j+1)
    if(flag):
        return True
    return False

def isInterleave(A, B, C):
    # Code here
    return check(A, B, C, 0, 0, 0)

t=int(input())
for i in range(t):
	arr=input().strip().split()
	if(isInterleave(arr[0],arr[1],arr[2])):
		print(1)
	else:
		print(0)
