sentence = input("Input the sentence")

vowelA = 0
vowelE = 0
vowelI = 0
vowelO = 0
vowelU = 0


length = len(sentence)

for letter in sentence:
    if letter == "a" or letter == "A": 
        vowelA = vowelA + 1
    elif letter == "e" or letter == "E":
        vowelE = vowelE + 1
    elif letter == "i" or letter == "I":
        vowelI = vowelI + 1
    elif letter == "o" or letter == "O":
        vowelO = vowelO + 1
    elif letter == "u" or letter == "U":
        vowelU = vowelU + 1


print(vowelA)
print(vowelE)
print(vowelI)
print(vowelO)
print(vowelU)