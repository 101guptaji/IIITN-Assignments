t=int(input())
t1=1
while(t>0):
	n=input()
	a=n
	if('4' in a):
		a=a.replace('1','0').replace('2','0').replace('3','0').replace('5','0').replace('6','0').replace('7','0').replace('8','0').replace('9','0')
		a=a.replace('4','2')
	print(a)
	b=n
	if('4' in b):
		b=b.replace('4','2')
	print(b)
	a=int(a)
	b=int(b)
	print('Case #%d:'%t1,a,b)
	t1+=1
	t-=1
