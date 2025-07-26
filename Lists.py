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
for i in range(len(numbers)):
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

#reversing
