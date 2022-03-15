phrase = input("Enter a word or phrase (without spaces or punctuation): ")

done = True
palindrome = True
start = 0

end = 0

while start < len(phrase):

    index = len(phrase) - 1
    end = int(phrase[index])
    if not start == end:
        palindrome = True
        
    start += 1
    end -= 1

if palindrome:
    print("That is a palindrome!")
else:
    print("That is not a palindrome.")
