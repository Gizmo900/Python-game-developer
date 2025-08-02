"""variable
"""
num=10  
#num is a variable name,= is used to assighn the value,10 is the value assigned

#list
num=[]   #empty list 
numbers=[90,30,20,60,5]
#to fetch any value from the list we consider the index number(position)the first index number is 0
print(numbers[2])
print(numbers[4])

#iteration
for i in range(len(numbers)): #len (numbers) tells how many things are in the list - for i in range go through every number in the list
    print(i) #prints index number 
    print(numbers[i]) #prints value placed at that location index number 

#len function
print(len(numbers)) #len function gives you number of elements present in the list

colours=["Red" ,"blue","green","yellow"]
#append function add-new element at the end of the list

colours.append("purple")
#add new element using user input
x=input("enter your color")
colours.append(x)
print(colours)

#insert function-add new element at a particular location
colours.insert(2,"black")   
print(colours)     
colours.insert(0,x)
print(colours)

#deleting elements 
colours.remove("Red")
print(colours)

# for loop-range(start,end,step)
#for i in range(100,49,-2):
    #print(i)
#reversing
#method 1
rev_list=[]
for i in range(len(colours)-1,-1,-1):
    rev_list.append(colours[i])
print(rev_list)

# method 2
colours.reverse()
print(colours)

#Sorting:Arranging elements in an ascending order
colours.sort()
print(colours)
#Slicing
print(colours[1:4]) #print element at index number 1 to 3