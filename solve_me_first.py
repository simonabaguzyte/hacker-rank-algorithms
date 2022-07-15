def solve_me_first(a,b):
    return a + b

if __name__ == '__main__':
    num1 = int(input("\nEnter first number: "))
    num2 = int(input("Enter second number: "))
    result = solve_me_first(num1,num2)
    print(f"Sum of entered numbers is: {result}")