def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


while True:
    choice = input(
        "Select the operation:\n"
        "1. Add:\n"
        "2. Subtract:\n"
        "3. Multiply:\n"
        "4. Divide:\n"
    )
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        choice = int(choice)

        if choice == 1:
            print(num1, '+', num2, ' = ', add(num1,num2))
        elif choice == 2:
            print(num1, '-', num2, ' = ', subtract(num1,num2))
        elif choice == 3:
            print(num1, '*', num2, ' = ', multiply(num1,num2))
        elif choice == 4:
            print(num1, '/', num2, ' = ', divide(num1,num2))

        next_calculation = input('Do you want perform more operations?: (yes/no): ')
        if next_calculation == 'no' or next_calculation == 'n':
            break
    else:
        print("Invalid input!")





