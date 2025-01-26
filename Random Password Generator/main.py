#Matthew McKinley Random Password Generator

import random
import string

#Checks input for number or boolean, error handler
def check_dataType(input_text, dataType, default = 0):
    #This checks for number values
    if dataType == 'float':
        for i in range(10):
            try:
                user_data = float(input(input_text))
                break
            except:
                print('That is not a number, try again.\n')
        else:
            print(f'Too many attempts, defaulted to {default}.')
            user_data = default
            #Boolean values
    if dataType == 'bool':
        user_data = input(input_text).lower()
        if user_data == 'n':
            user_data = False
        else:
            user_data = True
    return user_data

#Randomly generates each character in your password based off off the values you set
def randomNumGenerator(length, num, sym, upper, lower):
    password = ''
    for character in range(length):
        #Adds each character to this string
        possibleCharacters = ''
        if num: possibleCharacters += string.digits
        if sym: possibleCharacters += string.punctuation
        if upper: possibleCharacters += string.ascii_uppercase
        if lower: possibleCharacters += string.ascii_lowercase
        password += random.choice(possibleCharacters)
    return password

#Main UI, allows for multiple generations of passwords
def main():
    print('\033cWelcome to the random password generator.')
    print('This generator will generate 4 passwords for you after asking a few questions.')
    while True:
        length = int(check_dataType('How long would you like your password to be? --->  ', 'float', 10))
        numbers = check_dataType('Would you like to include numbers? (y/n) --->  ', 'bool')
        symbols = check_dataType('Would you like to include symbols? (y/n) --->  ', 'bool')
        upper = check_dataType('Would you like to include uppercase letters? (y/n) --->  ', 'bool')
        lower = check_dataType('Would you like to include lowercase letters? (y/n) --->  ', 'bool')
        if not numbers and not symbols and not upper and not lower:
            lower = True
        print('\033cHere are 4 randomly generated passwords: ')
        for i in range(4):
            #Generated password
            password = randomNumGenerator(length,numbers,symbols,upper,lower)
            # Prints 4 generated passwords
            print(f'{i+1}. {password}')
        #Allows for user to leave program
        if input('Would you like to generate more passwords? (y/n) --->  ').lower() == 'n':
            break
    
main()