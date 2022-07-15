def plusMinus(arr,n):
    # Write your code here
    arr_negative = []
    arr_positive = []
    arr_zero = []
    
    for i in arr:
        if i > 0:
            arr_positive.append(i)
        elif i < 0:
            arr_negative.append(i)
        elif i == 0:
            arr_zero.append(i)
                     
    proportion_of_positive = float(len(arr_positive) / n)
    proportion_of_negative = float(len(arr_negative) / n)        
    proportion_of_zero = float(len(arr_zero) / n)
    
    proportion_of_positive = ("{:.6f}".format(proportion_of_positive))
    proportion_of_negative = ("{:.6f}".format(proportion_of_negative))
    proportion_of_zero = ("{:.6f}".format(proportion_of_zero))
    
    return print(f"{proportion_of_positive}\n{proportion_of_negative}\n{proportion_of_zero}")


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr,n)
