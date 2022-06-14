#!/usr/bin/env python3

# Created by: Miguel Santacruz
# Created on: May 2022
# This program finds the average of numbers in a 2D array

import random


def average_of_numbers(rows, columns, a_2d_list):
    # this function finds the smallest number
    total = 0

    for row_value in a_2d_list:
        for column_value in row_value:
            total += column_value
    average = total / (rows * columns)

    return average


def main():
    # this function creates the array

    a_2d_list = []

    # input & process
    try:
        rows = int(input("Number of rows: "))
        columns = int(input("Number of columns: "))
        print("")
        if rows <= 0 or columns <= 0:
            print("Invalid input.")
        else:
            for rows_counter in range(0, rows):
                list_columns = []
                for columns_counter in range(0, columns):
                    random_number = random.randint(1, 50)
                    list_columns.append(random_number)
                a_2d_list.append(list_columns)
            for row_value in a_2d_list:
                print(row_value)
            answer = average_of_numbers(rows, columns, a_2d_list)
            print("The average is {}".format(answer))
    except Exception:
        print("")
        print("That's not valid input.")


if __name__ == "__main__":
    main()
