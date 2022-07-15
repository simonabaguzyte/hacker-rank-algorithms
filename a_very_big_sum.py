import math
import os
import random
import re
import sys

def aVeryBigSum(ar):
    sum = 0
    for i in ar:
        sum = sum + i    
    return sum
    
if __name__ == '__main__':
    ar_count = int(input().strip())
    ar = list(map(int, input().rstrip().split()))
    result = aVeryBigSum(ar)
    print(result)
