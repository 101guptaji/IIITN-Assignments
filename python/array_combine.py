A=[10,15,25]
B=[5,20,30]
n=len(A)
m=len(B)
c=[]
for i in range(n):
    x=A[i]
    for j in range(m):
        if(B[j]>x):
            c.append(x)
            c.append(B[j])
            break
        else:
            continue
    
