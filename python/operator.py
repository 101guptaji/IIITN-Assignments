import operator
x=input("enter two no.")
a,b=x.split()
a=int(a)
b=int(b)
print(a,"+",b,"=",operator.add(a,b))#a+b
print(a,"-",b,"=",operator.sub(a,b))#a-b
print(a,"*",b,"=",operator.mul(a,b))#a*b
print(a,"/",b,"=",operator.truediv(a,b))#a/b
print(a,"//",b,"=",operator.floordiv(a,b))#a//b
print(a,"**",b,"=",operator.pow(a,b))#a**b
print(a,"%",b,"=",operator.mod(a,b))#a%b

#relational operator
print(a,"<",b,":",operator.lt(a,b))
print(a,"<=",b,":",operator.le(a,b))
print(a,"=",b,":",operator.eq(a,b))
print(a,">",b,":",operator.gt(a,b))
print(a,">=",b,":",operator.ge(a,b))
print(a,"!=",b,":",operator.ne(a,b))

#Bitwise operation 
# using and_() to display bitwise and operation 
print ("The bitwise and of a and b is : ",end="") 
print (operator.and_(a,b)) #a & b

# using or_() to display bitwise or operation 
print ("The bitwise or of a and b is : ",end="") 
print (operator.or_(a,b)) #a| b

# using xor() to display bitwise exclusive or operation 
print ("The bitwise xor of a and b is : ",end="") 
print (operator.xor(a,b)) #a ^ b

# using invert() to invert value of a 
operator.invert(a) #~a

# printing modified value 
print ("The inverted value of a is : ",end="") 
print (a) 

