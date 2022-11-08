t=int(input())
s=t
l1=[]
while(t>0):
	a=input()
	n=len(a)
	x=0
	for i in range(n-2):
		if(a[i]=='g'):
			if(a[i+1]=='f'):
				if(a[i+2]=='g'):
					x+=1
	if(x>0):
		l1.append(x)
	else:
		l1.append("-1")
	t-=1

for i in range(s):
	print(l1[i])
    
