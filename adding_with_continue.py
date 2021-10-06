#!/usr/bin/env python3

# Created by: Crestel Ong
# Created on: October 2021
# This adding with continue and loop


def main():
    # this function ask for the amount of numbers you want to add
    # and then asks for each number to add then spits out the sum

    # declaring
    while_loop = 0
    total = 0

    # input
    number_of_loops_as_string = input("How many numbers do you want to add: ")
    print("")

    # have two trys because you need to check if the
    # number of numbers added and the added number are integers, you can't do
    # both in the same exception

    try:
        # convert string to integer
        number_of_loops = int(number_of_loops_as_string)

        # process and output

        while while_loop < number_of_loops:
            added_number_as_string = input("Enter a number to add:  ")
            added_number = int(added_number_as_string)

            try:

                if added_number < 0:
                    while_loop = while_loop + 1
                    continue

                else:
                    while_loop = while_loop + 1
                    total = total + added_number
                if while_loop == number_of_loops:
                    print("The sum of all the positive numbers is = {0}".format(total))
            except Exception:
                print("Invalid input.")

    except Exception:
        print("Invalid input.")

    print("\nDone.")


if __name__ == "__main__":
    main()
