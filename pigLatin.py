input_word = str(input("Enter a word: "))
vowels= "aeiouy"

while input_word != ".":
    if input_word == "":
        input_word = str(input("Enter a word: "))
        continue

    first_letter = input_word[0]
    if first_letter in vowels:
        print(input_word + "yay")


    else:
        i = 0
        for letter in input_word:
            if letter.lower() in vowels:
                i = input_word.index(letter)
                break
            
        print(input_word[i:]+input_word[:i]+"ay")
        
         
            
    
    input_word = str(input("Enter a word: "))
            
    
    

    
