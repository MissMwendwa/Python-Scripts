#this code is a function to create a dictionary
#It will also print out the square of the numbers
Num = dict() 
# this loop will give the squares for each key
#The range has to be between 1-21 so that the key 20 is included
for x in range (1,21):
    Num[x]= x**2
print(Num)
