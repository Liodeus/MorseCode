#!/usr/bin/env python
# - * -coding: utf - 8 - * -

import sys
import function as fun


def main():
    args = sys.argv

    if len(args) >= 2:
        print("Too many arguments")
    else:
        fun.choiseUser()

    test = '%s[!] %sNo help on' % (fun.Colors.R, fun.Colors.N)

    print(test)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("")
        sys.exit(0)
