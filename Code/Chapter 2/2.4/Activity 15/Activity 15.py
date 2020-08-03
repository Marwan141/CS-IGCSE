firstNames = ["Alex", "Bryn", "Eloise", "Lois", "James", "Sally"]

searchName = input("Please input the name your searching for.")

found = False
index = 0

while found == False and index <= (len(firstNames) - 1):
    if searchName == firstNames[index]:
        found = True
        
    index = index + 1

if found == True:
    print(str(searchName) + " is at position " + str(index) + " in the list ")
else:
    print(searchName + " is not in the list ")