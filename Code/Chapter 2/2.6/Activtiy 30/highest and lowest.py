def highLow(list):
    highest = max(list) #Function uses two built-in list methods
    lowest = min(list)
    return highest, lowest
#Main program
numbers = [12, 45, 1002, 3, 734, 0, -13, 950]
print(highLow(numbers))