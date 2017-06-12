#!/usr/bin/env python
# - * -coding: utf - 8 - * -

import sys
import function as fun

args = sys.argv

if len(args) >= 2:
    print("Too many arguments")
else:
    fun.choiseUser()
