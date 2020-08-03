exam1 = [25, 46, 71, 18, 31, 78, 92, 49, 63, 62, 11, 90, 83, 71, 41]
length = len(exam1) - 1
swapped = 1

while swapped == 1:
    swapped = 0
    for index in range(1, length):
        if exam1[index - 1] < exam1[index]:
            temp = exam1[index - 1]
            exam1[index - 1] = exam1[index]
            exam1[index] = temp
            swapped = 1

print(exam1[0])
print(exam1[length])