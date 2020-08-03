arrayForms = ["7AXB", "7PDB", "7ARL", "7JEH"]
form = input("Enter your form")

valid = False
index = 0
length = len(arrayForms)

while valid == False and index < length:
    if form == arrayForms[index]:
        valid = True
    index = index + 1
if valid == True:
    print("Valid Form")
else:
    print("The form you entered does not exist.")