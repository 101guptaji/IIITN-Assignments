'''Given three strings A, B and C your task is to complete the function isInterleave which returns true if C is an interleaving of A and B else returns false. C is said to be interleaving A and B, if it contains all characters of A and B and order of all characters in individual strings is preserved.'''
#Your task is to complete this Function \
#function should return True/False
def isInterleave(A, B, C):
    if len(A) == len(B) == len(C) == 0:
        return 1
    
    if len(C) == 0:
        return 0
    
    return (((len(C) and len(A) > 0) and (C[0] == A[0]) and isInterleave(A[1:], B, C[1:]))
        or ((len(C) and len(B) > 0) and (C[0] == B[0]) and isInterleave(A, B[1:], C[1:])))
    

# Your code goes here
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        arr=input().strip().split()
        if isInterleave(arr[0], arr[1], arr[2]):
            print(1)
        else:
            print(0)

