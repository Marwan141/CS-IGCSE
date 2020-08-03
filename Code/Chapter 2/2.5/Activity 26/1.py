#Stage 1
rawData = open("marks.txt", "r")
inputData = rawData.readlines()
rawData.close()

#Stage 2
examResults= []
index = 0
for line in inputData:
    examResults.append(inputData[index].split(","))
    index += 1
length = len(examResults)

#Stage 3
Total0 = 0
Total1 = 0
Total2 = 0
Total3 = 0

for learner in examResults:
    total0 += int(learner[1])
    total1 += int(learner[2])
    total2 += int(learner[3])
    total3 += int(learner[4])


print("Choose 1 if you want to see Lois Bennett's average mark")
print("Choose 2 if you want to see Eloise Roberts's average mark")
print("Choose 3 if you want to see James Hadwen's average mark")
print("Choose 4 if you want to see Patrick Dua-Brown's average mark")

choice = int(input("Choose one of the options."))

while choice >= 1 and choice <= 4:
    if choice == 1:
        print("The average mark is " + str(total0))
    elif choice == 2:
        print("The average mark is " + str(total1))
    elif choice == 3:
        print("The average mark is " + str(total2))
    elif choice == 4:
        print("The average mark is " + str(total3))
        
print("Input a correct option")