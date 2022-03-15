sentence = input("Please type a sentence: ")
accent = ""

index = 0
while index < len(sentence):
    if sentence[index] == "a"  or sentence[index] == "e" or sentence[index] == "i" or sentence[index] == "u":
        accent += "o"
    else:
        accent += sentence[index]
    index += 1
    
print("Here is your sentence with a weird accent:")
print(accent)
