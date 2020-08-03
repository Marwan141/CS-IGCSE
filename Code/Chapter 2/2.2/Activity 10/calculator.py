otherCalculation = "Y"

while otherCalculation == "Y":

    choice = int(input("Choose one of the options: 1. Addition 2. Substraction 3. Division 4. Multiplication"))
    if choice == 1 or choice == 2 or choice == 3 or choice == 4:
        break
    else:
        print('Invalid selection.')


    num1 = int(input("Input your first number"))
    num2 = int(input("Input your second number"))

    if choice == 1:
        print(num1 + num2)
    elif choice == 2:
        print(num1 - num2)
    elif choice == 3:
        print(num1 / num2)
    elif choice == 4:
        print(num1 * num2)

    otherCalculation = input("Do you want to do another calculation? Press Y for Yes or Press N for No")

