
my_int = int(input('Give me an int >= 0: '))

bstr = ""
while my_int > 0:
    quotient =my_int//2
    remainder = str(my_int % 2)
    my_int = quotient

    bstr = remainder+bstr

    print("The binary of", my_int, "is", bstr)

