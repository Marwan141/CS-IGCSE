lessons = 20

age = int(input("Please enter your age"))

if age > 18:
    extraLessons = (age-18)**2

else:
    pass
        

totalLessons = lessons + extraLessons
print("You have",totalLessons, "total lessons to do")