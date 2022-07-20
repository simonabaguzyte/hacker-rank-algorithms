import math
import os
import random
import re
import sys


def formingMagicSquare(matrix):

    matrix = sum(matrix, []) 
    magical_square = [[4, 9, 2, 3, 5, 7, 8, 1, 6], [8, 1, 6, 3, 5, 7, 4, 9, 2], [2, 9, 4, 7, 5, 3, 6, 1, 8], [4, 3, 8, 9, 5, 1, 2, 7, 6], [8, 3, 4, 1, 5, 9, 6, 7, 2], [6, 1, 8, 7, 5, 3, 2, 9, 4], [2, 7, 6, 9, 5, 1, 4, 3, 8], [6, 7, 2, 1, 5, 9, 8, 3, 4]]

    minimum_cost = sys.maxsize

    difference = 0
    for i in magical_square:
        for i,j in zip(matrix, i):
            difference = difference + abs(i-j)
        minimum_cost = min(minimum_cost, difference)

    return minimum_cost
    

if __name__ == '__main__':
    s = []

    for _ in range(3):
        s.append(list(map(int, input("\nEnter 3 rows of 3 positive integers: ").rstrip().split())))

    result = formingMagicSquare(s)
    print(result)
