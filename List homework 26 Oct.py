# get 20 random marks for 20 students (between 0 to 100)
#create three seperate lists 
# the first list should contain the marks  <=30
#the second list between 31 to 69
# the third list  >= 70

import random
#Get 20 random marks for 20 students (between 0 to 100)
marks=[] # An empty list named marks
for i in range(20):
    marks.append(random.randint(0,100))

# create 3 seperate lists based on the conditions
list1 = [] #an empty list to store marks that are 30 or less
list2 = [] 
list3 = [] 
for mark in marks: # a loop to look at each score(mark) in the marks list
    if mark <=30:
        list1.append(mark) # adds the mark to list1 if it is 30 or less
    elif 31 <= mark <= 69:
        list2.append(mark)
    else:
        list3.append(mark)

#Display the output lists 
print("Marks <= 30:", list1) #shows the list of marks that are 30 or less
print("Marks between 31 and 69:", list2)
print("Mark >= 70", list3)

























