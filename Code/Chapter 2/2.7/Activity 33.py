width = int(input("Enter the width "))
height = int(input("Enter the height "))

if width == 0 or height == 0:
    print("Please enter a number that is not 0 ")
else:
    area = width / height
    print("The area is: " + str(area))
