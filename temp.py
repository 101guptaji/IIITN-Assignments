#Each bridge initially claims that it itself is the root and sends the packet accordingly transmits the packet on all its adjcent lans. When it realises it is not the root, it only keeps updating the parameters(root, distance of root and RP) and transmits the update packets on the lan. Whenever there is nothing to be sent, it implies that the Root bridge and its distance from every other bridge along with the RP is found out and the program terminates.

n=int(input("enter the number of bridges "));
conn=[];

for i in range(0,n):
	#order by input be B1: A B C
	print("enter the connected lan to bride B"+str(i+1));
	a=input();
	conn.append(a);
lan=[]
for j in range(0,n):
	x=conn[j]
	l=x.split()
	br=l[0]
	l.remove(l[0])
	lan.append(l)
bri_conn=[]
#all_lan=[]
for k in range(0,n):
	bri_conn.append(0)

for i in range(0,n):
	y=[]
	for j in range(0,n):
		lanset1=set()
		lanset2=set()
		if(i!=j):
			z=lan[i]
			lanset1.update(z)
			z=lan[j]
			lanset2.update(z)
			common=lanset1.intersection(lanset2)
			#all_lan.append(lanset1.union(lanset2))
			if (common):
				y.append(j)
		bri_conn[i]=y
#print("all lans are:", all_lan);
print("bridge connection: ",bri_conn);
mess=[]
d=0
for i in range(0,n):
	mess_temp=['B'+str(i+1),d,'B'+str(i+1)]
	mess.append(mess_temp)
for i in range(n):
	tmp='B'+str(i+1)
	for j in bri_conn[i]:
		tmp2='B'+str(j+1)
		if(tmp>mess[j][0]):
			mess[i]=[mess[j][0],mess[j][1]+1,'B'+str(i+1)]
			tmp=mess[i][0]
print("config message for each bridge",mess);
