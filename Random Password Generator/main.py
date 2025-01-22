#Matthew McKinley Random Password Generator

#search google for "ascii characters" for the list thing, blue groups, and 'chr function python" for the chr function

#Create a program that allows a user to specify password requirements (length, upper/lowercase letters, numbers, and special characters) then gives them 4 possible passwords they could use. 

import random

def reqs():
    length = int(input("How many characters long do you want your password?"))
    uppercase = int(input("How many uppercase letters do you want in your password?"))
    lowercase = int(input("How many lowercase letters do you want in your password?"))
    numbers = int(input("How many numbers do you want in your password?"))
    special = int(input("How many special characters do you want in your password?"))
    if uppercase + lowercase + numbers + special == length:
        main()
    elif uppercase + lowercase + numbers + special != length:
        print("There is an error in the adding!")
        reqs()
        