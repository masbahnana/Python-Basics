# Multivalue variables
# Tuples
# Arrays
# Dictionaries

numberTuple = (1,2,3,4,5)
stringTuple = ("mammoth","abc","nimish")
itemTuple = ("fruit",2,5.5)
print("length of number tuple",len(numberTuple))
print("length of string tuple",len(stringTuple))
print("max of string tuple",max(stringTuple))
print("min of number tuple",min(numberTuple))
print("index of element 2",itemTuple.index(2))

groceryList = ["eggs","milk","flour","butter"]
print(groceryList)
print(groceryList[2:3])
groceryList[1] = "baking soda"
print(groceryList)
groceryList.append("milk")
print(groceryList)
groceryList.insert(2,"sugar")
print(groceryList)
groceryList.remove("butter")
print(groceryList)
del groceryList[1]
print(groceryList)
print("length of list is:",len(groceryList))
print("max of list is:",max(groceryList))
print("min of list is:",min(groceryList))

clothesList = ["t shirt","shorts","sunglasses"]
shoppingList = [groceryList,clothesList]
print(shoppingList)
print(shoppingList[1][0])
masterList = clothesList + groceryList
print(masterList)

listOfStudents = {0:"nimish",1:"jill",2:"harry",3:"lucy"}
print(listOfStudents)
print(listOfStudents[2])
listOfStudents[3] = "tanya"
print(listOfStudents)
print(listOfStudents.keys())
print(listOfStudents.values())