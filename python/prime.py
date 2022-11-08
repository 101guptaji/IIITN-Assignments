def isPrime(n):
    flag=0
    if(n>1):
        for i in range(2,n):
            if(n%i==0):
                flag=0
                break
            else:
                flag=1
        if(flag==1):
            return True
        else:
            return False
    else:
        return False

n=int(input())
print(isPrime(n))

