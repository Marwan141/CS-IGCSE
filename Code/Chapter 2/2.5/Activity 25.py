
marks =  [[80, 59, 34, 89], [31, 11, 47, 64], [29, 56, 13, 91], [55, 61, 48, 0], [75, 78, 81, 91]]

length = (len(marks) - 1)
for r in marks:
    for c in r:
        print(c,end = " ")
    print()


highestMark = marks[0][0]
lowestMark = marks[0][0]

total = 0 
count = 0 
for row in marks:
    for column in row:
        total += column
        count +=1
        if column > highestMark:
            highestMark = column
        elif column < lowestMark:
            lowestMark = column

print("To display the highest value choose 1")
print("To display the lowest value choose 2")
print("To display the average mark choose 3")
choice = int(input("Choose one of the options "))
validChoice = False
while validChoice == False:
    if choice == 1:
        print('The highest mark is', highestMark)
        validChoice = True
    elif choice == 2:
        print('The lowest mark is', lowestMark)
        validChoice = True
    elif choice == 3:
        print('The average mark is', total/count)
        validChoice = True
    else:
        print("Input a correct option")
        

