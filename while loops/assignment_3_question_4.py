#Write a program using a while statement, that given an int as the input, 
# prints all the factors of that number, one in each line.


n = int(input("Input an int: ")) # Do not change this line

counter = 1

while (counter <= n):
    if (n % counter == 0):
        print (counter)
    counter += 1

    

