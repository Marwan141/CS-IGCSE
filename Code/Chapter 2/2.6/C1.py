import numpy as np
from scipy import stats as sc
num1 = int(input("Enter your first number "))
num2 = int(input("Enter your second number "))
num3 = int(input("Enter your third number "))
arrayNum = [num1, num2, num3]


def calculator(num1, num2, num3):
    print("Option 1: Calculate mean")
    print("Option 2: Calculate mode")
    print("Option 3: Calculate median")

    choice = int(input("Choose an option"))

    while choice >= 1 and choice <= 3: 
        if choice == 1:
            mean = np.mean(arrayNum)
            print("The mean is " + str(mean))
        elif choice == 2:
            mode = sc.mode(arrayNum)
            print("The mode is " + str(mode))
        elif choice == 3:
            median = np.median(arrayNum)
            print("The median is " + str(median))
        else:
            print("Input a correct number")

print(calculator(num1, num2, num3))

