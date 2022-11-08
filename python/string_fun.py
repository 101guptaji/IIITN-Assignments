st="I love my tea"
str1="ltm"
str2="abc"
map=str.maketrans(str1,str2)
print("string befor map",st)
print("map value",map)
print("string after translation",st.translate(map))

#strip function
s2="++++m mar +++ java++++"
print("stripping all + string is",s2.strip('+'))
print("stripping strating + string is",s2.lstrip('+'))
print("stripping last + string is",s2.rstrip('+'))

#replace function
s3="koi mil gya koi kho gya koi mar gya"
str3="koi"
str4="dulha"
print(s3.replace(str3,str4,2))
