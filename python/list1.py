def get(): 
	print("ready")
	return "go"
def Main():
	print("started")
	print(get())
if __name__=="__main__":
	Main()

a=input("enter")
b=a.split()
print(b)
for i in range(len(b)):
	print(type(b[i]))
