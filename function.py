import morseCodeTable as m
import readline
import sys


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
# Interface and colors from : [recon-ng v4.9.1, Tim Tomes (@LaNMaSteR53)]
def choiseUser():
    print(
        "%s                    [Morse, Thibault Galbourdin (github.com/Liodeus)]" % (Colors.O))

    # Commands
    print("%s[1] cypher" % (Colors.B))
    print("%s[2] decypher" % (Colors.B))
    print("%s[3] help" % (Colors.B))
    print("%s[4] exit" % (Colors.B))
    print("%s" % (Colors.N))

    # Autocompletion
    completer = MyCompleter(["cypher", "decypher", "help", "exit"])
    readline.set_completer(completer.complete)
    readline.parse_and_bind('tab: complete')

    delimiter = ("%s---------------------------------------%s" %
                 (Colors.G, Colors.N))

    # Exit the program if user type -> exit
    while True:
        choiceUser = input("[Morse] > ")

        split = choiceUser.split(' ')

        # User want to cypher
        if split[0] == "cypher":
            if len(split) > 1:
                split.remove("cypher")
                print(cypher(' '.join(split).upper()))
            else:
                print(delimiter)
                print("Encrypt the sentence you enter \n")
                print("Usage : cypher [values]")
                print(delimiter)

        # User want to decypher
        elif split[0] == "decypher":
            if len(split) > 1:
                split.remove("decypher")
                print(decypher(' '.join(split).upper()))
            else:
                print(delimiter)
                print("Decrypt the sentence you enter \n")
                print("Usage : decypher [values]")
                print(delimiter)

        # User need help
        elif split[0] == "help":

            if len(split) == 1:
                print("Commands (type [help <topic>):             ")
                print(delimiter)
                print("cypher       Encrypt the sentence you enter")
                print("decypher     Decrypt the sentence you enter")
                print("help         Displays this menu            ")
                print("exit         Exit the program              ")
                print(delimiter)

            elif len(split) == 2:
                if split[1] == "cypher":
                    print(delimiter)
                    print("Encrypt the sentence you enter \n")
                    print("Usage : cypher [values]")
                    print(delimiter)
                elif split[1] == "decypher":
                    print(delimiter)
                    print("Decrypt the sentence you enter \n")
                    print("Usage : decypher [values]")
                    print(delimiter)
                else:
                    print('%s[!] No help on %s%s' %
                          (Colors.R, split[1], Colors.N))

        # User want to exit
        elif split[0] == "exit":
            sys.exit(0)

        # User type just enter
        elif split[0] == "":
            pass

        # Error
        else:
            print(split[0], ": not found")


# Colors use in the program
class Colors(object):
    N = '\033[m'  # native
    R = '\033[31m'  # red
    O = '\033[33m'  # orange
    G = '\033[32m'  # green
    B = '\033[34m'  # blue


# Use for autocompletion
class MyCompleter(object):

    def __init__(self, options):
        self.options = sorted(options)

    def complete(self, text, state):
        if state == 0:  # on first trigger, build possible matches
            if text:  # cache matches (entries that start with entered text)
                self.matches = [s for s in self.options
                                if s and s.startswith(text)]
            else:  # no text entered, all matches possible
                self.matches = self.options[:]

        # return match indexed by state
        try:
            return self.matches[state]
        except IndexError:
            return None
