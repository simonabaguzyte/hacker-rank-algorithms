
if __name__ == '__main__':

    number_of_elements = int(input("Enter number of elements for an array: "))
    
    sum_of_array_elements = 0
    count = 0
    while count != number_of_elements:
        input_value = int(input("Enter an element for an array: "))
        sum_of_array_elements = sum_of_array_elements + input_value
        count = count + 1

    print(sum_of_array_elements)