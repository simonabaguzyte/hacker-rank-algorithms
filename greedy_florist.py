#!/bin/python3

import math
import os
import random
import re
import sys


def getMinimumCost(flowers, prices, buyers):
    
    prices.sort(reverse=True)

    minimumCost = 0
    count = 0
    index = 0
    timesOfBuying = 0
    temporary = 0
    i = flowers - 1
    
    while count <= flowers:
        if buyers >= flowers:
            while index < len(prices):
                minimumCost = minimumCost + int(prices[index])
                index = index + 1

        elif buyers < flowers:
            while i >= 0:
                i = i - 1
                if temporary == buyers:
                    timesOfBuying = timesOfBuying + 1
                    temporary = 0
                    
                minimumCost = minimumCost + ((1 + timesOfBuying) * int(prices[index]))
                temporary = temporary + 1
                index = index + 1
                
        count = count + 1

    return minimumCost

    
if __name__ == '__main__':

    nk = input("\nEnter number of flowers and buyers: ").split()
    n = int(nk[0])
    k = int(nk[1])
    
    c = list(map(int, input("Enter price for each flower: ").rstrip().split()))

    minimumCost = getMinimumCost(n, c, k)

    print(minimumCost)