def fun(t1,a,b,n):
	a1=a
	b1=b
	while(b1%10!=4 and b1>0):
		b1=b1//10
	while(a1%10!=4 and a1>0):
		a1=a1//10
	if(b1%10!=4 and a1%10!=4 and a+b==n):
		print('Case #%d:'%t1,a,b)
	elif(b1%10==4):
		fun(t1,a+1,b-1,n)
	elif(a1%10==4):
	    fun(t1,a+1,b-1,n)
t=int(input())
t1=1
while(t>0):
	n=int(input())
	a=1
	b=n-a
	fun(t1,a,b,n)
	t-=1
	t1+=1

