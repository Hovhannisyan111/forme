#Guess the word
print("What is the capital of france: ")
capital = "paris"
ms = "-" * len(capital)

while "-" in ms:
    print(ms)
    letter = input("Enter a letter: ")
    
    for i in range (len(capital)):
        if capital[i] == letter:
            ms = ms[:i] + letter + ms[i + 1:]
print("You win: " , capital)
