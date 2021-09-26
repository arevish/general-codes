#Print the list of square and cube root of the number given by the user using lambda function
def sqr(a):
    return a*a
def cube(a):
    return a*a*a
func= [sqr, cube]
i= int (input("Enter the  number you want cube and square root of = "))
for i in range (1,i+1):
    val = list( map(lambda x:x(i),func))
    print(i, "=", val)
