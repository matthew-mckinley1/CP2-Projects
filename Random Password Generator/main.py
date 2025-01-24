#Matthew McKinley Random Password Generator

#search google for "ascii characters" for the list thing, blue groups, and 'chr function python" for the chr function

#Create a program that allows a user to specify password requirements (length, upper/lowercase letters, numbers, and special characters) then gives them 4 possible passwords they could use. 

import random

def reqs():
    length = int(input("How many characters long do you want your password?"))
    uppercase = int(input("Do you want uppercase letters in your password? (Y/N)"))
    lowercase = int(input("Do you want lowercase letters in your password? (Y/N)"))
    numbers = int(input("Do you want numbers in your password? (Y/N)"))
    special = int(input("Do you want special characters in your password? (Y/N)"))
    #for x in length:
        #while x <= length:
            