from ast import Return


def birthdayCakeCandles(arr):

    length = len(arr)
    arr.sort()
    highest_number = arr[len(arr) - 1]
    repetition_of_highest_number = 1
    index = length - 2

    while index >= 0:
        if arr[index] == highest_number:
            repetition_of_highest_number = repetition_of_highest_number + 1
            index = index - 1
        else:
            index = index - 1

    return repetition_of_highest_number


if __name__ == '__main__':

    candles_count = int(input("\nEnter number of candles: ").strip())

    candles = list(map(int, input("Enter an integer for every candle: ").rstrip().split()))

    result = birthdayCakeCandles(candles)
    print(f"There are/is {result} tallest candle/candles")