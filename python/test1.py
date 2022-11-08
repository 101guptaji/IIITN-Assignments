from collections import Counter

def arrayManipulation(n, queries):
    c = {}
    for a,b,k in queries:
        c[a] =c.get(a,0)+k
        c[b+1]=c.get(b+1,0)-k
        print(c)
    arrSum = 0
    maxSum = 0
    t=sorted(c)[:-1]
    print("sorted",t)
    for i in sorted(c)[:-1]:
        print(i)
        arrSum+= c[i]
        maxSum = max(maxSum,arrSum)
    return maxSum

n,m = map(int,input().split())
queries = [list(map(int,input().split())) for _ in range(m)]
print(arrayManipulation(n, queries))
