n=int(input())
arr=list(map(int,input().split()))

print(arr)
n=len(arr)
sum1=min(arr)
for i in range(n):
    for j in range(i+1,n+1):
        #print(arr[i:j])
        if(sum1<sum(arr[i:j])):
            sum1=sum(arr[i:j])
print(sum1)