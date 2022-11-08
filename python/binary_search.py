def bs(l1,low,mid,high,s):
	if(s==l1[mid]):
		return mid
	elif(s<l1[mid]):
		#low=0
		high=mid
		mid=(low+high)//2
		return bs(l1,low,mid,high,s)
	elif(s>l1[mid]):
		low=mid
		#high=n-1
		mid=(low+high)//2
		return bs(l1,low,mid,high,s)
	else:
		print("not found")

n=int(input("enter size of array"))
l1=[]
for i in range(n):
	x=int(input())
	l1.append(x)
s=int(input("enter search element"))
mid=n//2
pos=bs(l1,0,mid,n-1,s)
print("element",s,"found at index",pos)
