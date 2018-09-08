#A prime number is a whole number greater than 1 whose only factors are 1 and itself.

#Write a program using a while statement, that given an int as the input, 
#prints out "Prime" if the int is a prime number, otherwise it prints "!Prime".


n = int(input("Input a natural number: "))

counter = 2 #ég byrja á 2 því það er ekki hægt að deila með núlli og allar tölur eru deilanegar með 1 
prime = n > 1
while counter < n and prime
    if n % counter == 0:
        print("Prime")

    else:
        print("!Prime")

 #af hverjuuuuuu!?