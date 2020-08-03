marks =  [[80, 59, 34, 89], [31, 11, 47, 64], [29, 56, 13, 91], [55, 61, 48, 0], [75, 78, 81, 91]]

length = (len(marks) - 1)
for r in marks:
    for c in r:
        print(c,end = " ")
    print()


highestMark = marks[0][0]
lowestMark = marks[0][0]

total = 0 
count = 0 
for row in marks:
    for column in row:
        total += column
        count +=1
        if column > highestMark:
            highestMark = column
        elif column < lowestMark:
            lowestMark = column
print('The highest mark is', highestMark)
print('The lowest mark is', lowestMark)
print('The average mark is', total/count)

