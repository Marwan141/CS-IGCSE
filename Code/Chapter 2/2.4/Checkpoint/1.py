addressBook = [["Marwan", "y********@gmail.com"]]

addNew = "Y"
name = ""
email = ""
while addNew == "Y":
    name = input("What is the name of the new contact? ")
    email = input("What is the email of the new contact? ")
    addNew = input("Do you want to add another contact? Press Y for Yes or any other key for No ")
    newAddressBook = [name, email]
    addressBook.append(newAddressBook)

searchName = input("Please input the name of the contact you're searching for. ")
found = False
index = 0

while found == False and index <= (len(addressBook) - 1):
    if searchName == addressBook[index][0]:
        print("The email address is", addressBook[index][1])
        found = True
    else:
        index = index + 1
    if found == False:
        print("The contact your searching for was not found")

