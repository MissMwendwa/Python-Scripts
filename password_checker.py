#in order to begin we have to import a module
import re

#request the user to enter their password
password =input("Kindly Input your password: ")

#here we start the password checking exercise as per the criteria
P = True
while P:
    if(len(password)<6 or len(password)>12):
        break
    elif not re.search("[a-z]", password):
        break
    elif not re.search("[A-Z]", password):
        break
    elif not re.search("[0-9]", password):
        break
    elif not re.search("[$#@]", password):
        break
    elif re.search("\s", password):
        break
    else:
        print("The password is valid")
        print(password)

        P = False
        break
if P:
    print("Invalid password. Please Try again!")


