import morseCodeTable as m


# Function cypher take a string as parameter
def cypher(stringToCypher):
    stringCypher = " "

    # For each letter in stringToCypher
    for letter in stringToCypher:

        # Space case
        if letter == " " and stringCypher[-1] != '/':
            stringCypher += ' /'

        # Alphabet case
        elif letter in m.Alphabet:
            stringCypher += ' ' + m.Alphabet[letter]

        # Number case
        elif letter in m.Numbers:
            stringCypher += ' ' + m.Numbers[letter]

        # Punctuation case
        elif letter in m.Punctuations:
            stringCypher += ' ' + m.Punctuations[letter]

        # Undefined case
        else:
            stringCypher += ' |'

    return stringCypher


# Function decypher take a string as parameter
def decypher(stringToDecypher):
    stringDecypher = " "

    # Split morse code
    wordMorse = stringToDecypher.split(" ")

    # For each word in wordMorse
    for word in wordMorse:

        # Alphabet case
        if word in m.morseToAlphabet:
            stringDecypher += m.morseToAlphabet[word]

        # Number case
        elif word in m.morseToNumbers:
            stringDecypher += m.morseToNumbers[word]

        # Punctuation case
        elif word in m.morseToPunctuation:
            stringDecypher += m.morseToPunctuation[word]

        # Undefined case
        else:
            stringDecypher += ' '

    return stringDecypher


# Function that display what command you can use
def choiseUser():
    # Command
    print("[1] cypher")
    print("[2] decypher")
    print("[3] help")
    print("[4] exit")
    print()

    choiceUser = ""

    # Exit the program if user type -> exit
    while choiceUser != "exit":
        choiceUser = input("[Morse] > ")

        split = choiceUser.split(' ')

        # User want to cypher
        if split[0] == "cypher":
            if len(split) > 1:
                split.remove("cypher")
                print(cypher(' '.join(split).upper()))
            else:
                print("---------------------------------------")
                print("Encrypt the sentence you enter \n")
                print("Usage : cypher [values]")
                print("---------------------------------------")

        # User want to decypher
        elif split[0] == "decypher":
            if len(split) > 1:
                split.remove("decypher")
                print(decypher(' '.join(split).upper()))
            else:
                print("---------------------------------------")
                print("Decrypt the sentence you enter \n")
                print("Usage : decypher [values]")
                print("---------------------------------------")

        # User need help
        elif split[0] == "help":
            if len(split) == 1:
                print("-------------------------------------------")
                print("cypher       Encrypt the sentence you enter")
                print("decypher     Decrypt the sentence you enter")
                print("help         Displays this menu            ")
                print("exit         Exits the program             ")
                print("-------------------------------------------")
            elif len(split) == 2:
                if split[1] == "cypher":
                    print("---------------------------------------")
                    print("Encrypt the sentence you enter \n")
                    print("Usage : cypher [values]")
                    print("---------------------------------------")
                elif split[1] == "decypher":
                    print("---------------------------------------")
                    print("Decrypt the sentence you enter \n")
                    print("Usage : decypher [values]")
                    print("---------------------------------------")
                else:
                    print("[!] No help on", split[1])

        # Error
        else:
            print(split[0], ": not found")
