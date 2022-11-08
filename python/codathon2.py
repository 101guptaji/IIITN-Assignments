l=int(input())
m=int(input())
n=int(input())
k=int(input())

def test(l,m,n,k):
	i=0
	while(l>0 or m>0 or n>0):
		s=k
		if(n>0):
			n-=1
			s-=1

		x=0
		y=0
		while(s>0 and abs(x-y)<1):
			if(l>0):
				l-=1
				s-=1
				x+=1
				if(m>0 and s>0):
					m-=1
					s-=1
					y+=1
			elif(m>0 and s>0):
				m-=1
				s-=1
				y+=1
			else:
				break
		i+=1
	print(i)
test(l,m,n,k)
