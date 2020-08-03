#While...DO loop

import random

diceRoll = random(range(1,7))

numb = int(input("Please enter a number between 1 and 6"))

while numb != diceRoll:
    numb = int(input("Please enter a number between 1 and 6"))

print("Well done, you've guessed correctly.")


#Repeat...Until Loop
while True:
    numb = int(input("Please enter a number between 1 and 6"))
    if numb = diceRoll:
        break

print("Well done, you've guessed correctly.")