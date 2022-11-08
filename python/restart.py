import os
r=input("do u want to restart the pc? yes/no")
if(r=='no'):
	exit()
else:
	os.system("shutdown /r /t 1");
