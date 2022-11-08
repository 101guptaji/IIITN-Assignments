x=input()
N,k=x.split()
N=int(N)
k=int(k)
l=[]
for i in range(N):
	a=int(input())
	l.append(a)

def fir(l,k):
	if(l[0]<k or l[0]==k):
		del l[0]
		fir(l,k)
	#print(l)

def last(l,k):
	if(l[-1]<k or l[-1]==k):
		del l[-1]
		last(l,k)
	#print(l)
fir(l,k)
last(l,k)
print(len(l))

