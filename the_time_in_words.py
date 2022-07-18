import math
import os
import random
import re
import sys

def timeInWords(h, m):
    numbers = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'twenty one', 'twenty two', 'twenty three', 'twenty four', 'twenty five', 'twenty six', 'twenty seven', 'twenty eight', 'twenty nine', 'thirty','thirty one', 'thirty two', 'thirty three', 'thirty four', 'thirty five', 'thirty six', 'thirty seven', 'thirty eight', 'thirty nine', 'forty', 'forty one', 'forty two', 'forty three', 'forty four']

    converted_into_words = ''

    minute = 'minute'
    if m > 1:
        minute = minute + 's'

    if m >= 00 and m <= 60: 
        if m == 00:
            converted_into_words = converted_into_words + numbers[h] + " o' clock"
        elif m == 15:
            converted_into_words = converted_into_words + "quarter past " + numbers[h]
        elif m == 30:
            converted_into_words = converted_into_words + "half past " + numbers[h]
        elif m == 40:
            converted_into_words = converted_into_words + "twenty minutes to " + numbers[h + 1]
        elif m == 45:
            converted_into_words = converted_into_words + "quarter to " + numbers[h + 1]
        elif m == 60:
            converted_into_words = converted_into_words + numbers[h + 1] + " o' clock"
        elif m < 30:
            converted_into_words = converted_into_words + numbers[m] + " " + minute + " past " + numbers[h]
        elif m > 30 and m < 45:
            converted_into_words = converted_into_words + numbers[m] + " " + minute + " past " + numbers[h]
        elif m > 45:
            converted_into_words = converted_into_words + numbers[60 - m] + " " + minute + " to " + numbers[h + 1]

    return converted_into_words

if __name__ == '__main__':

    h = int(input("\n\nEnter the hours portion: ").strip())

    m = int(input("\nEnter the minutes portion: ").strip())

    result = timeInWords(h, m)

    print(result)
