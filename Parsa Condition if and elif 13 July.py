
""" Date : 12/07/2025
Homework : Compute the total, percentage and grade of a student depending on the marks in his 5 subjects (maths,english,science,spanish,art ) and name.

Grade
A - 90-100
B - 71-89
C - 50-70
D - 40-49
Can do better - less than 40  """



"""day=input("What day is it?").lower()
holiday=input("Is it holiday today?yes/no ").upper()
print(day)
if day == "saturday":
    print("python classes")

elif day == "monday" and holiday=="YES":
    print("you can stay at home")
else:
    print("its a school day") """

name=input("What is your name?")
math=int(input("What was your math score?"))
if math>100:
    print("Mark should be <=100")
    exit()
english=int(input("What was your english score?"))
if english>100:
    print("Mark should be <=100")
    exit()
science=int(input("What was your science score?"))
if science>100:
    print("Mark should be <=100")
    exit()
spanish=int(input("What was your spanish score?"))
if spanish>100:
    print("Mark should be <=100")
    exit()
art=int(input("What was your art score?"))
if art>100:
    print("Mark should be <=100")
    exit()

if math>100 or english>100 or science>100 or spanish>100 or art>100:
    print("Mark should be <=100")
    exit()


total=math+science+spanish+english+art
percentage = total/5


if percentage>=90:
    print("Grade A")
elif percentage>=71:
    print("Grade B")
elif percentage>=50:
    print("Grade C")
elif percentage>=40:
    print("Grade D")
else:
    print("Grade Can do better")     
    

