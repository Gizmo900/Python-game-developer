
# Practice Tasks: Python Dictionary & List Exercises

# Date: 20/09/2025

#Task A: Library Management System
#Task 1: Create a Dictionary
#Create a dictionary named book with the following details:
#"title": The Great Gatsby
#"author": F. Scott Fitzgerald
#"year": 1925
#"copies": 4
#Your tasks:
#Print the value of "title".
#Print the entire dictionary.


book={ "title":"The great Gatsby",
              "year":1925,
              "copies":4,
              "author":"F. Scott Fitzgerald"}

print("title:", book["title"])
print("book:",book)





# Task 2: Compare Dictionary and List
#Create a list containing the same book information.
#Your tasks:
#Print the first element of the list.
#Print the "title" from the dictionary.


book_list=["The Great Gatsby", "F.Scott Fitzgerald", 1925, 4]

print("\nTask 2")
print("1) First element of the list:", book_list[0])
print('2) "title" from the dictionary:',book["title"])
print(book["title"])

#Write down the difference between accessing data from 
#a list and a dictionary. 

##Lists → Access by index (position).Example:Book_list[0] → "The Great Gatsby"
# Dictionaries → Access by key. Example: Book["title"] → "The Great Gatsby"


#Task 3: Display Keys and Values
#Using the book dictionary:
#Print all keys using .keys().
#Print all values using .values().
#Loop through the dictionary and print each key and its value.  

print("\nTask 3")
for key,value in book.items():  #.items() returns all the key–value pairs in the dictionary.
    
    print(key,value)

#Task 4: Check if a Key Exists
#Check if the key "publisher" exists in the dictionary:
#If it exists, print the value.
#If it does not exist, print "Publisher information not available". 


print("\nTask 4")
if "publisher" in book:
    print("publisher:",book["publisher"])
else:
    
    print("publisher:","Publisher information not available")


#Task 5: Add and Delete Keys
#Add a new key "genre" with the value "Fiction".
#Print the updated dictionary.
#Delete the "genre" key.
#Print the dictionary again to confirm deletion. """


print("\nTask 5")
book["genre"]="fiction"
print("book:",book)

del book ["genre"]
print("book:",book)



# Task 6: Modify Values
#Update the "copies" to 6.
#Print the updated dictionary.  


print("\nTask 6")
book ["copies"]=6
print("book:",book)






# Task 7: Store a List as a Value


#Add a new key "reviews" with the value as a list:
#["Excellent", "Very Good", "Classic Literature"]
#Print the dictionary.
#Print the second review from the "reviews" list.  

print("\nTask 7")
#Add a new key"reviews" = with a list of reviews.
book["reviews"] = ["Excellent", "Very good","Classic Literature"]

# Print the updated dictionary
print("book:", book)

#Print the second review (index 1,since lists start at 0)
print("Second review:",book["reviews"][1])




  
#Task B: Create a Nested Dictionary

#Create a dictionary called library with the following data:

#B001:
#title: The Great Gatsby
#author: F. Scott Fitzgerald
#year: 1925
#copies: 6
#reviews: ["Excellent", "Very Good"]

#B002:
#title: To Kill a Mockingbird
#author: Harper Lee
#year: 1960
#copies: 3
#reviews: ["Inspirational", "Heart-touching"]

#Your tasks:

#Print the title of book B001.
#Print all the book IDs (keys of library).
#Update the number of copies for B002 to 5.

#nested dictionary

library={
    "BOO1":{
        "Title":"The Great Gatsby",
        "Author":"F. Scott Fitzgerald",
        "Year":1925,
        "Copies":6,
        "Reviews":["Excellent", "Very Good"],
    },

      
   "BOO2":{
      "Title":"To kill a mocking bird",
      "Author":"Harper Lee",
      "Year":1960,
      "Copies":3,
      "Reviews":["Inspirational,Heart-touching"],
   }
      
      
}

#1.  Print the title of BOO1
print("\nTask B1")
print("Title of BOO1:", library["BOO1"]["Title"])

#2. print all the book IDs  (keys of library)
print("\nTask B2")
print("Book IDs:", library.keys ())

#3. Update the number of copies for BOO2 to 5
print("\nTask B3")
library["BOO2"]["copies"]=5
print("Updated copies of BOO2:", library["BOO2"]["copies"])



#Add a new book B003 with your own details.
# B003:
#"title": "1984",
#"author": "George Orwell",
#"year": 1949,
#"copies": 4,
#"reviews": ["Thought-provoking", "Classic"]

#4.Add a new book (BOO3)
print("\nTask B4")
library["B003"] = {
    "title": "1984",
    "author": "George Orwell",
    "year": 1949,
    "copies": 4,
    "reviews": ["Thought-provoking", "Classic"]
}
print("Added BOO3:", library["B003"])

#5.Delete book B001 from the dictionary.
print("\nTask B5")
del library["BOO1"]
print("Library after deleting BOO1:", library)