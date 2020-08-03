import random
anotherGo = "Y"
while anotherGo == "Y":
    row = random.randint(0, 3)
    column = random.randint(0, 3)
    found = False
    print("The treasure map consists of a grid of four rows and four columns.")

    while not found:
        rowGuess = int( input('Enter a random row: '))
        columnGuess = int(input('Enter a random column: '))
        print(rowGuess, columnGuess)
        if rowGuess == row and columnGuess == column:
            found = True
            print("You've found the treasure.")
        elif rowGuess == row:
            print("Correct row but the column is wrong. Try again.")
        elif columnGuess == column:
            print("Correct column but the row is wrong. Try again.")
        else:
            print("Give it another go")
anotherGo = input('Do you want to try again? Press Y to continue. ')