#combining 2 strings
print('vishal' + 'vishal')

#print name 10 times
print(10*'vishal \n ')

#delete number from the list
#numbs(15,14,12)

numb = [12,36,45,15,14,12,78,98]
del numb[3:6]
print(numb)

# make alist from list print only number grreater than 6
list = ["Vishal",7,"kumar",67,89,168,"fourty","twenty",6,5,36,1]
for item in list:
    if str(item).isnumeric() and item > 6:
        print(item)