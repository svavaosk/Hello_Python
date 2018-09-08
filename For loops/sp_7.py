#Write a Python program using a for loop that, given a integer n, prints out all the Armstrong number between 0 and n.  
# You can assume that the maximum is 999.
#An Armstrong number is a number that is equal to the sum of its digits when each digit is raised to the number of digits.

#For example:
#6 is an Armstrong number because 6**1 = 6
#153 is an Armstrong number because 1**3 + 5**3 + 3**3 = 153

top_num = int(input("Input a number between 0 and 999: "))

n= top_num
for i in range(0,n):
    num=i
    result=0
    power =len(str(i)) #fjöldi tölustafa í tölu (þarf að vera string því það er "collection/sequence")
    while(i!=0):
        digit = i % 10 
        result += digit**power 
        i=i//10
    if num == result:
        print(num)


    
