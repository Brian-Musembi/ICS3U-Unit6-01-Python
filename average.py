#!/usr/bin/env python3

# Created by Brian Musembi
# Created on June 2021
# This program prints 10 random integers and finds the average

import random


def main():
    # This function prints 10 random integers and finds their average

    print("This program prints 10 random integers, between 1 and 100, "
          "and finds their average.")
    print("")

    random_list = []

    print("Displayed below are 10 random integers between 1 and 100:")

    # process
    for loop_counter in range(0, 10):
        # random number
        random_number = random.randint(1, 100)
        random_list.append(random_number)
        print(random_number)

    average = (sum(random_list)) / 10

    print("")
    print("The average of these 10 random integers is: {0}".format(average))


if __name__ == "__main__":
    main()
