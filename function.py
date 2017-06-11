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
            stringCypher += '|'

    return stringCypher


# Function decypher take a string as parameter
def decypher(stringToDecypher):
    stringDecypher = " "

    return stringDecypher
