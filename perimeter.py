#first we have to import the math module to be able to perform any mathematicla operration
from math import sqrt 

perimeter = 0

#this part of the code prompts the user to input the values
first_x = float(input("Enter the x part of the coordinate: "))
first_y = float(input("Enter the y part of the coordinate: "))

#this should get values from repeating the above process
prev_x = first_x
prev_y = first_y

#this prompts the blank to quit activity
line = input("Enter the x part of the coordinate (blank to quit): ")

#this loop will determine how many times the user will be able to be prompted to input values
while line != "":
  x = float(line)
  y = float(input("Enter the y part of the coordinate: "))

#this block calculates the perimeter
  dist = sqrt((prev_x - x ) ** 2 +(prev_y - y) ** 2)
  perimeter = perimeter + dist 

  prev_x = x 
  prev_y = y 
  line = input("Enter the x part of the coordinate (blank to quit): ")

  dist = sqrt((first_x - x) ** 2 + (first_y - y) ** 2)
  perimeter = perimeter + dist

  print(f"The perimeter of that polygon is {perimeter}")