albumDetails = {"Title"}

title = input("Please input the title of the album. ")
year = int(input("Please input the year of release of the album. "))
genre = input("Please input the genre of the album. ")
newalbum =
details = {"Title": title, "Year": year, "Genre": genre}

details.append()

print(details)

searchItem = input("Please input the name of the album you want to search for")

if searchItem == details["Title"]:
    print("Your album's details are: " + str(details))