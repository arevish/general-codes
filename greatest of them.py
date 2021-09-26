#take 3 number and find greatest of them
a= int(input("Enter your 1st number "))
b= int(input("Enter your 2nd number "))
c = int(input("Enter yopur 3rd number "))
if a>b:
    if a>c:
        print(a, " is the greatest number!")
    else :
        print(c, " is the greatest number")
else:
     print(b, " is the greatest number")       