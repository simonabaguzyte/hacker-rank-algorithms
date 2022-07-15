def staircase(number_of_stairs):

    space = ' '
    symbol ='#'

    count = 1
    while count <= number_of_stairs:
        if count < number_of_stairs:
            print((number_of_stairs-count-1)*space,count*symbol)
            count = count + 1
        elif count == number_of_stairs:
            print(count*symbol)
            count = count + 1

if __name__ == '__main__':
    number_of_stairs = int(input("\nEnter number of stairs: ").strip())
 
    staircase(number_of_stairs)
