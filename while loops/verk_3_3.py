num = int(input("Input an int: "))
#gefið er að alltaf byjra í einum
#fyrsta sem við gerum er að búa til counter breytu
counter = 0
odd_number = 1 

while counter < num:
    print(odd_number)
    odd_number += 2
    counter += 1 
    # ^það sama og að segja counter = counter + 1
    #það má koma hvað sem er inn í while statement, t.d. if setning eða önnur while loop.

#önnur leið: (ekki jafn skýr)
#while counter < num: 
    #print(counter *2 +1)
    #counter +=1