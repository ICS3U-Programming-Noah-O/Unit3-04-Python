#!/usr/bin/env python3
# Created By: Noah Ouellette
# Date: Dec. 9, 2021
# This program allows a user inpit a number
# and then detect if it is 0, positive, or negative.

import colorama
import random
import time
from colorama import Fore, Back, Style


def main():

    # Get user input and print intro text
    print(Fore.WHITE + "This program can detect positive or negative numbers!")
    time.sleep(1)
    print(Fore.BLUE + " ")
    user_num = float(input("Enter your number: "))

    # Process/Output: Evaluate if the user input is positive, negative, or 0
    # Loop after every answer
    time.sleep(1)
    print(Fore.CYAN + " ")
    if user_num == 0.0:
        print("{} is 0.".format(user_num))
        print("")
        time.sleep(1)
        main()
    elif user_num < 0:
        print("{} is negative.".format(user_num))
        print("")
        time.sleep(1)
        main()
    else:
        print("{} is positive.".format(user_num))
        print("")
        time.sleep(1)
        main()


if __name__ == "__main__":
    main()
