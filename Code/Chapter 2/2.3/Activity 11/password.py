password = input("Please input your password.")

length = len(password)

if length < 6:
    print("The password you have entered is not long enough")
else:
    print("Lenght of password is OK")