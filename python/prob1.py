t=int(input())
while(t>0):
	c1,c2=map(int,input().split())
	l1=[]
	l2=[]
	s1=s2=0
	    #x=int(input())
	l1.extend(map(int,input().split()))
	print(l1)    
	l2.extend(map(int,input().split()))
	print(l2)   
	t-=1
	p1=len(l1)
	p2=len(l2)
	for i in range(p1):
		s1+=l1[i]
	for i in range(p2):
		s2+=l1[i]
	if(s1>s2):
		print("C1")
	else:
		print("C2")
