# Calculadora

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def pow(a,b):
    b = 2
    return a ** b

def calculator():
    while True:
        print("\nSimple Calculator")
        print("Options:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Pow")
        print("6. Exit")
        choice = input("Select an operation (1/2/3/4/5/6): ")
        if choice == '6':
            print("Exiting calculator.")
            break
        if choice in ('1', '2', '3', '4', '5'):
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                if choice == '1':
                    print(f"Result: {num1} + {num2} = {add(num1, num2)}")
                elif choice == '2':
                    print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
                elif choice == '4':
                    print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
                elif choice == '5':
                    print(f"Result: {num1} pow 2 = {pow(num1)}")
        else:
            print("Invalid choice. Please select a valid option.")
calculator()