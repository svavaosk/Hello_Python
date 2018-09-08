#range er fall sem getur búið til eitthvað bil
for number in range (0,5):
    print("number is now",number)

# við getum ekki alltaf notað for lúpu, t.d notandi þarf að slá inn tölu sem má ekki vera jaafn og tíu, þá er betra að nota while. 

name = "batman"

for letter in name:
    if letter == "a":
        print("i found the letter a")
    print(letter)

#other_x = 0
#while other_x < 5:
    #print(other_x)

    # mikilvægt að átta sig á að þetta x í for 
    # loopinu gerir það sama og er í while loouni, 
    # þar þurfum við ekki að hugsa um að hækka gildið eitthvað.