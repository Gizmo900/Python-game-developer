
"""Homework 23rd August


Add a Cartoon – Add a new cartoon to your favorites list.

Insert a Cartoon at a Spot – Add a cartoon in a specific position (e.g., 1st, 2nd, etc.).

Remove a Cartoon – Take a cartoon off your list.

Show My List – Display all your favorite cartoons.

Reverse, Sort, and Slice – Try reversing, sorting, and slicing the cartoons list.

Slicing Task – Print elements at index positions 3 to 5.

Example list:
spongebob, tom, jerry, donald duck, mickey mouse
  """

# Start with a list of cartoons
cartoons=["Donald duck","Tom","Jerry","Mickey mouse"]

#append()- adds a new element at the end of the list
cartoons.append("Woody woodpecker")
print (cartoons)

#add element using user input
x=input("Enter your cartoon:")#Ask the user for a cartoon name
cartoons.append(x) #Add it to the end of the list 
print (cartoons) # Show the list

#insert()- Adds a new element at a particular location
cartoons.insert(2, "Bugster bunny") #Put "Bugster bunny" at position 2
print (cartoons) #Show the list

cartoons.insert(0,x) #Insert the user's cartoon at the very start
print(cartoons) #Show the list


#remove()- deletes an element
cartoons.remove("Donald duck") #Remove "Donald duck" from the list
print(cartoons) #show the list

#Reverse()- reverses the list order
cartoons.reverse()
print("Reversed list:", cartoons)

#Sort()- sorts the list alphabetically (A to Z)
cartoons.sort()
print("Sorted list:", cartoons)

#Slicing- get a part of the list
print("Slicing [3:6]",cartoons[3:6]) #Get items from index 3 up to 5






