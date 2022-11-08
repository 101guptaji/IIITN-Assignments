#code without using map, filter and lambda 

# Find the number which are odd in the list 
# and multiply them by 5 and create a new list 

# Declare a new list 
x = [2, 3, 4, 5, 6] 

# Empty list for answer 
y = [] 

# Perform the operations and print the answer 
for v in x: 
	if v % 2: 
		y += [v*5] 
print (y) 

#above code with map, filter and lambda 

# Declare a list 
x = [2, 3, 4, 5, 6] 

# Perform the same operation as in above post 
y = map(lambda v : v * 5, filter(lambda u : u % 2, x)) 
print (y) 

