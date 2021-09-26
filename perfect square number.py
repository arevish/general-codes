#print all the perfect square of numbers from 1 to the number taken from the user
print("Perfect Squares")
a=int(input("Please Enter the last number "))
for i in range (1,a , 1):
    print("Perfect square of ", i)
    i*=i
    print(i)