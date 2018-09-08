#If a chessboard were to have wheat placed upon each square such that one grain were placed on the first square,
# two on the second, four on the third, and so on (doubling the number of grains on each subsequent square), 
# how many grains of wheat would be on the chessboard at the finish?
#Write a Python program using a for loop that calculates and prints out this number of grains.

#2 er töfratala í tölvunarfræði
#binary= talnakerfi sem notað eru tvö tákn (0 og 1)
# 2^0 =1 2^1=2 2^2=4 2^3=8 2^4=16 2^5=32....

grain = 0 #byrjum á því að hafa ekkert korn

for grain in range(1,65): #bilið okkar er 1-64 sem er fjöldi reita á taflborðinu. 
    grain += 2**(x-1) #viljum fá 2^0 og upp að 2^63
print (grain)

#byrja á að hafa summu = 0
#leggja saman hvern og einn reit
#