 
import string
sentence = str(input("Enter a sentence: "))

count_of_upper = 0 
for letter in sentence:
    if letter.isupper():
        count_of_upper +=1 
print("{:>15}{:>5}".format("Upper case", count_of_upper))


count_of_lower = 0
for letter in sentence:
    if letter.islower():
        count_of_lower  += 1
print("{:>15}{:>5}".format("Lower case",count_of_lower))


count_of_digits = 0
for i in sentence:
    if i.isdigit():
        count_of_digits +=1
print("{:>15}{:>5}".format("Digits",count_of_digits))


count_of_punctuation= 0
for i in sentence:
    if i in string.punctuation:
        count_of_punctuation += 1
print("{:>15}{:>5}".format("Punctuation",count_of_punctuation))