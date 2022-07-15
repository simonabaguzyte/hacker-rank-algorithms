import math
import os
import random
import re
import sys

def compareTriplets(alice_points, bob_points):
    alice_points = 0
    bob_points = 0
   
    if a[0] < b[0]:
        bob_points = bob_points + 1
    elif a[0] > b[0]:
        alice_points = alice_points + 1
        
    if a[1] < b[1]:
        bob_points = bob_points + 1
    elif a[1] > b[1]:
        alice_points = alice_points + 1
        
    if a[2] < b[2]:
        bob_points = bob_points + 1
    elif a[2] > b[2]:
        alice_points = alice_points + 1
            
    points = [alice_points, bob_points]
    return points

if __name__ == '__main__':
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    result = compareTriplets(a, b)
    print(result)