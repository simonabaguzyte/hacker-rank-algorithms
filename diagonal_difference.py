def diagonal_difference(arr, number_of_rows_and_columns):
    
    sum_of_left_to_right_diagonal = 0
    sum_of_right_to_left_diagonal = 0
    
    for i in range(number_of_rows_and_columns):
        sum_of_left_to_right_diagonal = sum_of_left_to_right_diagonal + arr[i][i]
        sum_of_right_to_left_diagonal = sum_of_right_to_left_diagonal + arr[i][number_of_rows_and_columns-1-i]
    
    return abs(sum_of_left_to_right_diagonal - sum_of_right_to_left_diagonal)

    
if __name__ == '__main__':

    number_of_rows_and_columns = int(input("\nEnter number of rows for matrix: ").strip())
    arr = []
    for _ in range(number_of_rows_and_columns):
        arr.append(list(map(int, input("Enter 3 integers for every row: ").rstrip().split())))

    result = diagonal_difference(arr, number_of_rows_and_columns)
    print(f"Absolute diagonal difference is: {result}")