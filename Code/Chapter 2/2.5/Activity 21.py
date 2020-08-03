validChoice = False


while validChoice == False:
    option = int(input("Welcome! To check average temperature please input '1'" "To check the temperature range please input '2' " "To check the wind speed please input '3' " "If you want to quit the program input '4'" ))
    if option >= 1 and option <= 4:
        print("You have chosen a correct option!")
        validChoice = True
        if option == 1:
            print("You want to check the average temperature")
        elif option == 2:
            print("You want to check the temperature range")
        elif option == 3:
            print("You want to check the wind speed")
        elif option == 4:
            print("Quitting the program... ):")
    else:
        print("Enter another number")

