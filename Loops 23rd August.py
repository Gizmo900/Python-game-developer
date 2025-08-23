#print 50 to 100
#for loop
for i in range(50,101):
    print(i)
#while loop
counter = 50
while counter<=100:
    print (counter)
    counter = counter+1

#search the number
numbers = [3,78,90,32,57]
search=int(input("Enter the number you want to search "))
for i in range(len(numbers)):
    if search==numbers[i]:
        print("The number is present at index ",i)
        break
else:
        print("The number is not present")    

     