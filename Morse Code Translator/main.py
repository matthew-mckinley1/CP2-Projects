#Matthew McKinley Morse Code Translator

#list of letters in english and morse
english = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
morse = [".-", "-...", "-.-.", "-.", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

#changing the english input to morse code
def eng_to_morse(english, morse):
    #take the input of what they want to change from english to morse
    engCode = input("What would you like to change to morse code?")
    #current list of what the changed is
    result = []
    #iterating through and appending the list
    for i in engCode:
        for item in english:
            if i == item:
                result.append(morse[english.index(item)])
    #printing that and going to the main UI
    print(result)
    main(english, morse)
                
#changing the morse code input to english
def morse_to_eng(english, morse):
    #takint the input of what they want to change from morse to english
    morseCode = input("What would you like to change to english? Use | to start a new word. :")
    morseCode = morseCode.split()
    resulty = []

    #iterating through the list of morse code and appending the result list
    for i in morseCode:
        for item in morse:
            if i == item:
                resulty.append(english[morse.index(item)])
            elif i == "|":
                resulty.append(" ")
                break
    #result list
    resulty = "".join(resulty)
    #printing the result list
    print(resulty)
    #resetting to the main function
    main(english, morse)

#main function
def main(english, morse):
    #asking them which option they want to change
    choice = int(input(" Press 1 to turn English into Morse Code \n Press 2 to turn Morse Code into English \n Press 3 to exit \n :"))
    #if their choice is something, do something else
    if choice == 1:
        eng_to_morse(english, morse)
    elif choice == 2:
        morse_to_eng(english, morse)
    elif choice == 3:
        exit()
    #else if their choice is not one of those, then tell them and let them retry
    else:
        print("This is not an acceptable input! Try again!")
        main(english, morse)

#calling the main function to start the code
main(english, morse)