word = str(input("Enter a word: "))
vowel= "a" or "e" or "i" or "o" or "u" 

while word != ".":
    while word[0]!= vowel:
        word[1:]+word[0]
    print(word + "ay")
    
    else:
        print(word + "yay")