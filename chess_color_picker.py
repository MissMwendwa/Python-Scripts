'''This code python script will use strings to determine the cell colors
Since we are not error checking then the code will be less than 10 lines
We will convert the values into integers and add the integers to get odd and even numbers
The even numbers will be black while the odd ones will be white'''
#Inputting the letters of the cells

label = "abcdefgh"

#prompt the user to input the cell 
cell = input("Enter the cell index: ")

#the code to determine the column and the row posisitions
col_pos = int(label.index(cell[0]))+1
row_pos = int(cell[-1])

#this is where the if block starts and it identifies whether the cell is black or white
pos = row_pos + col_pos

if pos%2 == 1:
    print("The cell is white")
else:
    print("The cell is black")