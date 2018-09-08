#Write a Python program using for loops that, given an integer n, prints all the perfect numbers from 1 to n.

#A perfect number is an integer whose sum of integer divisiors (excluding the number itself) add up to the number.

#For example, 6 is a perfect number because the sum of its integer divisors (1+2+3) is equal to 6.

top_num = int(input("Upper number for the range: "))
n= top_num

for  num in range (1, (n+1)):
    sum_of_divisors = 0
    for i in range (1, num):
        if num % i == 0:
            sum_of_divisors += i
    if num == sum_of_divisors:
        print(num,"is a perfect number")



