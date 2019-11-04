#!/usr/bin/env python3

# Created by: Trinity Armstrong
# Created on: October 2019
# This program uses a for loop


def main():
    # this function uses a for loop

    # input
    positive_integer = int(input("Enter a positive integer: "))
    print("")

    # process & output
    for counter in range(positive_integer + 1):
        square = counter**2
        print("{0}² = {1}".format(counter, square))


if __name__ == "__main__":
    main()
