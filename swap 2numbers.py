#swap 2 numbers
a=5
b=7
n=a
a=b
b=n
print(a,  b)

# swap number without third variable
a=6
b=5
a=a+b
b=a-b
a= a-b
print("a=" ,a ,"b= " ,b)

#other short way
a=5
b=6
a,b=b,a
print("a= ",a ,"b=" ,b)

#using xor method
a=5
b=6
a=a^b
b=a^b
a=a^b
print("a= ",a,"b=",b)