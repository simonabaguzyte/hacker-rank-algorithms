def countApplesAndOranges(s_house_starts, t_house_ends, a_apple_tree, b_orange_tree, apples_array, oranges_array):
    def find_if_in_range(position):
        return position >= s_house_starts and position <= t_house_ends

    count_apples = 0
    count_oranges = 0

    for apple_position in apples_array:
        if find_if_in_range(apple_position + a_apple_tree):
            count_apples += 1

    for orange_position in oranges_array:
        if find_if_in_range(orange_position + b_orange_tree):
            count_oranges += 1
            
    print(count_apples)
    print(count_oranges)

    
if __name__ == '__main__':
    
    house_position = input("\nEnter starting and ending point of the house: ").rstrip().split()

    s = int(house_position[0])

    t = int(house_position[1])

    apple_orange_tree_position = input("Enter position of apple and orange tree: ").rstrip().split()

    a = int(apple_orange_tree_position[0])

    b = int(apple_orange_tree_position[1])

    apple_orange_fruit_number = input("Enter number of apples and oranges: ").rstrip().split()

    m = int(apple_orange_fruit_number[0])

    n = int(apple_orange_fruit_number[1])

    apples = list(map(int, input("Enter position of apples: ").rstrip().split()))

    oranges = list(map(int, input("Enter position of oranges: ").rstrip().split()))

    # countApplesAndOranges(7, 10, 4, 12, [2, 3, -4], [3, -2, -4]) #test

    countApplesAndOranges(s, t, a, b, apples, oranges)
