#Matthew McKinley Morse Code Translator

english = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
morse = [".-", "-...", "-.-.", "-.", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]


def engToMorse(english, morse):
    engCode = input("What would you like to change to morse code?")
    result = []


    for i in engCode:
        for item in english:
            if i == item:
                result.append(morse[english.index(item)])
    print(result)
    main(english, morse)
                
def morseToEng(english, morse):
    morseCode = input("What would you like to change to english? Use | to start a new word. :")
    morseCode = morseCode.split()
    resulty = []

    for i in morseCode:
        for item in morse:
            if i == item:
                resulty.append(english[morse.index(item)])
            elif i == "|":
                resulty.append(" ")
                break
    resulty = "".join(resulty)
    print(resulty)
    main(english, morse)


def main(english, morse):
    choice = int(input(" Press 1 to turn English into Morse Code \n Press 2 to turn Morse Code into English \n Press 3 to exit \n :"))
    if choice == 1:
        engToMorse(english, morse)
    elif choice == 2:
        morseToEng(english, morse)
    elif choice == 3:
        exit()
    else:
        print("This is not an acceptable input! Try again!")
        main(english, morse)

main(english, morse)