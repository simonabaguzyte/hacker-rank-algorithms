def miniMaxSum(arr):
    arr.sort()
    sum_of_array_elements = sum(arr)
    max_sum = sum_of_array_elements - arr[0]
    min_sum = sum_of_array_elements - arr[len(arr) - 1]
    print(min_sum, max_sum)
        
if __name__ == '__main__':
    arr = list(map(int, input("\nEnter five integers: ").rstrip().split()))
    miniMaxSum(arr)
