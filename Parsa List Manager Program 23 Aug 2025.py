""" Homework 23rd August 2025:
List Manager Program
A. Create a program that will allow the user to easily manage a list of names.
 You should display a menu that will allow them to add a name to the list, 
 change a name in the list, delete a name from the list or view all the names in the list.
There should also be a menu option to allow the user to end the program. 
If they select an option that is not relevant, then it should display a suitable message. 
After they have made a selection to either add a name, change a name, delete a name or 
view all the names, they should see the menu again without having to restart the program. 
The program should be made as easy to use as possible.

B. Try reversing, sorting and slicing on the cartoons list
Slicing – print element at index, 3 to 5   """


# Name List Program
names=[]

# Showing the menu again and again until the user decides to quit
while True:
    print("What would you like to do?")
    print("1.Add a name")
    print("2.Change a name")
    print("3.Delete a name")
    print("4.View all the names")
    print("5.Exit")
    
    choice= input("Type a number (1,2,3,4,5):")

    #option 1:add a name
    if choice== "1":
        new_name= input("Type the name you want to add:")
        if new_name.isalpha():
            names.append(new_name)
            print("Name added!")
        else:
            print("Please enter a valid name")

    


    #option 2:Change a name
    elif choice== "2":
        old_name= input("Type the name you want to change:")
        if old_name in names:
            new_name=input("Type the new name")
            index=names.index(old_name)#finds where that name is in the list and 
                                   #and saves it in the variable index.
            names[index]=new_name
            print("Name changed")
        
        else:
            print("That name is not in the list")
 
    # Option 3:Delete a name
    elif choice== "3":
        name_delete= input("Type the name you want to delete:")
        if name_delete in names:
           names.remove(name_delete)
           print("Name deleted!")
        else:
           print("That name is not in the list")

# Option 4:View all names.
    elif choice== "4":
        print("Here are the names in the list:")
        for name in names:#For loop goes through each name in the list called names,
                          #one by one.Each time the current name will be stored in a
                          #temperorary variable called name.
            print(name)

# Option 5:Exit the code
    elif choice== "5":
    
        print("Goodbye!")
        break # The break command stops the loop completely and make a program
               # Exit the while loop Trup:loop. 

    #if the user types something wrong   
    else:
        print("Invalid choice,try again")

    


