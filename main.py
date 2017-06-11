#!/usr/bin/env python
# - * -coding: utf - 8 - * -

# import sys
import function as fun

# args = sys.argv# print(args)
userInput = input("Enter something to cypher : ").upper()

test = fun.cypher(userInput)
test2 = fun.decypher(test)

print(test)
print(test2)
