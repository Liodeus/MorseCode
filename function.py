import morseCodeTable as m
import readline
import sys
import os


# Function cypher take a string as parameter
def cypherSentence(stringToCypher):
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

# Function cypherFile take 2 parameters
# pathFile -> the file you want to cypher
# outputPath -> the file you want to save the cypher


def cypherFile(pathFile, outputPath):
    if os.path.exists(pathFile):
        try:
            file = open(outputPath, "w")
            with open(pathFile, "r") as inFile:
                for line in inFile:
                    # Write the cypher in outputPath
                    file.write(cypherSentence(line.upper()))
            file.close()
        except:
            print("%sError the output path you gave is wrong !%s" %
                  (Colors.R, Colors.N))

    else:
        print("%sError the path you gave is wrong !%s" % (Colors.R, Colors.N))


# Function decypher take a string as parameter
def decypherSentence(stringToDecypher):
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


# Function decypherFile take 2 parameters
# pathFile -> the file you want to decypher
# outputPath -> the file you want to save the decypher
def decypherFile(pathFile, outputPath):
    if os.path.exists(pathFile):
        try:
            file = open(outputPath, "w")
            with open(pathFile, "r") as inFile:
                for line in inFile:
                    # Write the decypher in outputPath
                    file.write(decypherSentence(line.upper()))
            file.close()
        except:
            print("%sError the output path you gave is wrong !%s" %
                  (Colors.R, Colors.N))

    else:
        print("%sError the path you gave is wrong !%s" % (Colors.R, Colors.N))


# Function that display what command you can use
# Interface and colors from : [recon-ng v4.9.1, Tim Tomes (@LaNMaSteR53)]
def choiseUser():
    print(
        "%s                    [Morse, Thibault Galbourdin (github.com/Liodeus)]" % (Colors.O))

    # Commands
    print("%s[1] cypher -n | -f" % (Colors.B))
    print("%s[2] decypher -n | -f" % (Colors.B))
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
            try:
                # Cypher a sentence
                if(split[1] == "-n"):
                    split.remove("cypher")
                    split.remove("-n")
                    print(cypherSentence(' '.join(split).upper()))

                # Cypher a file
                elif(split[1] == "-f"):
                    cypherFile(split[2], split[3])

            except:
                print(delimiter)
                print("cypher -n")
                print("    Encrypt a sentence")
                print("    Usage: cypher -n [sentence] \n")
                print("cypher -f")
                print("    Encrypt a file")
                print("    Usage: cypher -f <pathFile> <outputPath>\n")
                print(delimiter)

        # User want to decypher
        elif split[0] == "decypher":
            try:
                # Decypher a sentence
                if(split[1] == "-n"):
                    split.remove("decypher")
                    split.remove("-n")
                    print(decypherSentence(' '.join(split).upper()))

                # Decypher a file
                elif(split[1] == "-f"):
                    decypherFile(split[2], split[3])
            except:
                print(delimiter)
                print("decypher -n")
                print("    Decrypt a sentence")
                print("    Usage : decypher -n [sentence]\n")
                print("decypher -f")
                print("    Decrypt a file")
                print("    Usage : decypher -f <pathFile> <outputPath>\n")
                print(delimiter)

        # User need help
        elif split[0] == "help":
            if len(split) == 1:
                print("Commands (type [help <topic>]):             ")
                print(delimiter)
                print("cypher       Encrypt the sentence or file you enter")
                print("decypher     Decrypt the sentence or file you enter")
                print("help         Displays this menu            ")
                print("exit         Exit the program              ")
                print(delimiter)

            elif len(split) == 2:
                if split[1] == "cypher":
                    print(delimiter)
                    print("cypher -n")
                    print("    Encrypt the sentence you enter")
                    print("    Usage: cypher -n [sentence] \n")
                    print("cypher -f")
                    print("    Encrypt a file")
                    print("    Usage: cypher -f <pathFile> <outputPath> \n")
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
