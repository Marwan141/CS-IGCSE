text = input("Input your text ") 
newText = ""
code = ""
length = len(text) - 1
index = 0

while length + 1 == 0:
    text = input("Input your text ") 

for i in text:
    if length == 0:
        run = 1
        code = code + str(run)
        code = code + text[index]
        print(code)
    else:
        run = 1
        newText = text[index]
        index = index + 1
        if index <= length - 1:
            if text[index] == newText:
                run = run + 1
                index = index + 1
                code = code + str(run)
                code = code + newText
                print(code)
            else:
                code = code + run
                code = code + newText
                run = 1
                newText = text[index]
                index = index + 1
        else:
            code = code + str(run)
            code = code + newText
            print(code)

        
#Failed Attempt ^^^

#Answer
def rle_encode(string):
    encoding = ''
    prev_char = ''
    count = 1

    if not string: return ''

    for char in string:
        # If the prev and current characters
        # don't match...
        if char != prev_char:
            # ...then add the count and character
            # to our encoding
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            # Or increment our counter
            # if the characters do match
            count += 1
    else:
        # Finish off the encoding
        encoding += str(count) + prev_char
        return encoding


