firstName = input("Please input your first name")
lastName = input("Please input your last name")



while len(lastName) < 4:
    lastName = lastName + "X"


print(lastName)
username = lastName[:4] + firstName[:1]
print("Your username is " + username)