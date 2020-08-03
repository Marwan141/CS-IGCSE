total = 0
enterNumber = int(input("Please input the enter number"))
endNumber = int(input("Please end the end number"))

for index in range(enterNumber, (endNumber + 1)):
    print(total + index)