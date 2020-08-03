import random


parkCharge = random.randint(1, 2000)
payment = 0
while payment < parkCharge or payment > 20:
    print("The charge is", parkCharge)
    int(input("Please enter payment up to 20€ maximum"))
    changeDue = payment - parkCharge


    while changeDue >= 10:
        print("10€ Note")
        changeDue = changeDue - 10
    while changeDue >= 5:
        print("5€ Note")
        changeDue = changeDue - 5
    while changeDue >= 2:
        print("2€ Coin")
        changeDue = changeDue - 2
    while changeDue >= 1:
        print("1€ Coin")
        changeDue = changeDue - 1
    while changeDue >= 0.5:
        print("0.5€ Coin")
        changeDue = changeDue - 0.5
    while changeDue >= 0.1:
        print("0.1€ Coin")
        changeDue = changeDue - 0.1
    while changeDue >= 0.05:
        print("0.05€ Coin")
        changeDue = changeDue - 0.05
    while changeDue >= 0.02:
        print("0.02€ Coin")
        changeDue = changeDue - 0.02
    while changeDue >= 0.01:
        print("0.01€ Coin")
        changeDue = changeDue - 0.01
    
    