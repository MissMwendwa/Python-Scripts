'''This block of code is to help the user find the best approximation to Pi
It will prompt the user to enter a number between 1-50
That will determine the maximum number of iterations'''
#the code of the iterating method will be written here
def find_pi(max_val):
    sum = 0

    # this loop will determine the iteratons to find the most accurate value
    for i in range(1,max_val+1):
        sum = sum + ((-1)**(i+1))*(1/((2*i)*(2*i+1)*(2*1+2)))

    #this will print the value of sum
    print(4*sum+ 3)

#call the method to execute
find_pi(50)
        

