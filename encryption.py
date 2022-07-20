import math
import os
import random
import re
import sys


def encryption(s):
    encrypted_message = ''

    s_without_spaces = s.replace(" ", "")
    s_length = len(s_without_spaces)

    s_length_root = math.pow(s_length, 0.5)
    rows = round(s_length_root)
    columns = math.ceil(s_length_root)

    print(s_without_spaces)
    print(s_length)
    print(s_length_root)
    print(rows)
    print(columns)

    s_in_rows_and_columns = []

    for i in range(columns):
        encrypted_message = encrypted_message + s_without_spaces[i::columns] + " "

    return encrypted_message


if __name__ == '__main__':
    s = input("\nEnter string: ")
    result = encryption(s)
    print(result)

