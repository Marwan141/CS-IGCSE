import random2
validGuess = "Y"

correct = random2.randint(1,6)
guess = int(input("Input a number between 1 and 6 "))

if guess < 0 or guess > 7:
    print("Input a correct number")
    validGuess = "N"

while validGuess == "Y":
    if guess == correct:
        print("Well Done!")
        validGuess = "N"
    else:
        print("Try again.")
        validGuess = "N"

