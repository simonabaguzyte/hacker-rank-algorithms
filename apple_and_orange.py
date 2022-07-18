def countApplesAndOranges(s_house_starts, t_house_ends, a_apple_tree, b_orange_tree, apples_array, oranges_array):
    
    adding_apple_distance_to_position_of_tree = []
    adding_orange_distance_to_position_of_tree = []
    
    for i in apples_array:
        adding_apple_distance_to_position_of_tree = adding_apple_distance_to_position_of_tree + [a_apple_tree + i]
    
    for i in oranges_array:
        adding_orange_distance_to_position_of_tree = adding_orange_distance_to_position_of_tree + [b_orange_tree + i]
        
    count_apples_on_house = 0
    count_oranges_on_house = 0

    for i in adding_apple_distance_to_position_of_tree:
        if i >= s_house_starts and i <= t_house_ends:
            count_apples_on_house = count_apples_on_house + 1

    for i in adding_orange_distance_to_position_of_tree:
        if i >= s_house_starts and i <= t_house_ends:
            count_oranges_on_house = count_oranges_on_house + 1

    return print(f"{count_apples_on_house}\n{count_oranges_on_house}")

    
if __name__ == '__main__':
    
    first_multiple_input = input("\nEnter starting and ending point of the house: ").rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input("Enter position of apple and orange tree: ").rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input("Enter number of apples and oranges: ").rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input("Enter position of apples: ").rstrip().split()))

    oranges = list(map(int, input("Enter position of oranges: ").rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
