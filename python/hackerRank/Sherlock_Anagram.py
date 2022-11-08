s='mom'
n=len(s)
res=0
d={}
for i in range(n):
	
	for j in range(i+1,n+1):
		sub=''.join(sorted(s[i:j]))
		if(sub not in d):
			d[sub]=1
		else:
			d[sub]+=1
		res+=d[sub]-1
		print(sub,d,res)
print(res)
