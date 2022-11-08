t=int(input())
s=t
l4=[]
while(t>0):
	c=int(input())
	l1=[]
	l1.extend(map(int,input().split()))
	#print(l1)
	
	s1=0
	p1=len(l1)
	while(p1>0):
		x=max(l1)
		s1+=x
		#print(s1)
		l1.remove(x)
		y=x-1
		if(y in l1):
			l1.remove(y) 
		
		p1=len(l1)
	l4.append(s1)
	t-=1
#print(l4)
for i in range(s):
	print(l4[i])
	


	
	
