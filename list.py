mylist = [] #this is how you tell python you want a variable of the type called list
mylist.apppend(1) #this is how you add an item to a list giving us mylist = [1]
mylist.append(2) #you add another item (this time 2, so mylist = [1, 2] 
mylist.append(3) #mylist = [1,2,3] now

#how to print or show the content of mylist
print(mylist[0]) #prints 1
print(mylist[1]) #prints 2
print(mylist[2]) #prints 3

'''
Note: Counting starts with 0 though we tend to pay no attention to this.
so mylist[0] is the first item followed by mylist[1] and mylist[2] and should we 
have more it follows that way
'''
#Now to print everything inside the mylist we use what is called a loop
#More details on loop please shortly

for myitem in mylist:
	print(myitem)
