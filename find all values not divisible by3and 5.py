#print all the numbers from 1 to the last number given by the user and skipping number divisible by 3 or 5
a = int(input("Enter your last number "))
i=1
while i<=a:
    r= i%3 and i%5
    if r!=0:
        print(i)
    i= i+1