
"""Homework 2nd August

➕ Add a Cartoon – Add a new cartoon to your favorites list.

✏️ Insert a Cartoon at a Spot – Add a cartoon in a specific position (like 1st, 2nd, etc.).

🗑️ Remove a Cartoon – Take a cartoon off your list.

🧾 Show My List – See all your favorite cartoons. 

spongebob,tom,jerry,donald duck,mickey mouse
  """

"""variable
"""
num=10  
#num is a variable name,= is used to assighn the value,10 is the value assigned

#list
num=[]   #empty list 
numbers=[90,30,20,60,5]#This is a list of numbers which can be summoned when typing its index number
#to fetch any value from the list we consider the index number(position)the first index number is 0
print(numbers[2])
print(numbers[4])

#iteration
for i in range(len(numbers)):  #len (numbers) tells how many things are in the list - for i in range go through every number in the list
    print(i) #prints index number 
    print(numbers[i]) #prints value placed at that location index number 

#len function
print(len(numbers)) #len function gives you number of elements present in the list

cartoons=["Donald duck" ,"Tom","Jerry","Mickey mouse"]
#append function add-new element at the end of the list

cartoons.append("Woody woodpecker")
#add new element using user input
x=input("enter your cartoon")#Asks the question enter your cartoon
cartoons.append(x)#
print(cartoons)#prints cartoons

#insert function-add new element at a particular location
cartoons.insert(2,"Bugster bunny")   
print(cartoons) #prints the cartoons    
cartoons.insert(0,x)
print(cartoons)#prints the cartoons

#deleting elements 
cartoons.remove("Donald duck")#removes the donald duck cartoon from the list
print(cartoons)#prints cartoons

#reversing










""" """
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
  """
