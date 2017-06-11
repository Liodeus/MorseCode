# -*- coding: utf-8 -*-

import morseCodeTable as m

userInput = input("Enter something to cypher : ").upper()

for letter in userInput:

    if letter in m.Letters:
        print(m.Letters[letter])

    elif letter in m.ListNumbers:
        if letter == '0':
            index = "zero"
        elif letter == '1':
            index = "one"
        elif letter == '2':
            index = "two"
        elif letter == '3':
            index = "three"
        elif letter == '4':
            index = "four"
        elif letter == '5':
            index = "five"
        elif letter == '6':
            index = "six"
        elif letter == '7':
            index = "seven"
        elif letter == '8':
            index = "height"
        elif letter == '9':
            index = "nine"

        print(m.Numbers[index])

    elif letter in m.ListPunctuations:
        if letter == '.':
            index = "point"
        elif letter == ',':
            index = "comma"
        elif letter == '?':
            index = "questionMark"
        elif letter == '-':
            index = "minus"
        elif letter == '=':
            index = "equal"
        elif letter == ':':
            index = "colon"
        elif letter == ';':
            index = "semicolon"
        elif letter == '(':
            index = "parentheseLeft"
        elif letter == ')':
            index = "parentheseRight"
        elif letter == '/':
            index = "slash"
        elif letter == '"':
            index = "quotationMark"
        elif letter == '$':
            index = "dollar"
        elif letter == '\'':
            index = "apostrophe"
        elif letter == '_':
            index = "dash"
        elif letter == '@':
            index = "atSign"
        elif letter == '!':
            index = "exclamationMark"
        elif letter == '+':
            index = "plus"
        elif letter == '~':
            index = "tilde"
        elif letter == '#':
            index = "hashtag"
        elif letter == "&":
            index = "ampersand"

        print(m.Punctuations[index])
