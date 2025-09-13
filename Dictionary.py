#create empty dictonary
mydictionary={}

detail={"name":"Parsa",
        "age":11,
        "country":"UK"}

print("mydictionary:",mydictionary)
print("detail:",detail)


#Accesing values
print("country:",detail["country"])
print("age:",detail["age"])

#Adding items
detail["hobby"]="badminton"
print("detail:",detail)

#modify value/update
detail["age"]=70
print("detail:",detail)

#removing 
del detail["hobby"]
print("detail:",detail)

#check if present or if not present
if "age"in detail:         
    print("Age detail:", detail["age"])
else:
    print("Age not present")

if "hobby"in detail:
    print("hobby detail:", detail["hobby"])
else:
    print("hobby not present")
 
#Length of dictionary
print("len detail:",len(detail))

# store a list as a value
detail["clubs"]=["Lego club","Minecraft club","chess club"]

#Get the list of keys 
print(detail.keys())

#Get a list of values
print(detail.values())

#Print the key value pair in a single line
for key,value in detail.items():
    print(key,value)

    #nested dictionary
classroom={
    "Parsa":{
        "Age":11,
        "height":160,
    },
    "John":{
        "Age":11,
        "height":155,
    }
}
print(classroom)
print(classroom["Parsa"])
print(classroom["John"]["height"])








