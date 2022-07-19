import math
import os
import random
import re
import sys


def extraLongFactorials(n):
    answer = n
    count = 1
    count2 = 1
    
    while count <= n:
        while count2 <= n - 1:
            answer = answer * (n - count2)
            count2 = count2 + 1 
        count = count + 1      
    
    return print(answer)

if __name__ == '__main__':
    n = int(input("\nEnter an integer: ").strip())

    extraLongFactorials(n)