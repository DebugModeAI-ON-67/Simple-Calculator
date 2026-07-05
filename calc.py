import os


def add(x, y):
    answer = x + y
    print("\nSum: " + str(answer))


def sub(x, y):
    answer = x - y
    print("\nDifference: " + str(answer))


def mult(x, y):
    answer = x * y
    print("\nProduct: " + str(answer))


def div(x, y):
    try:
        answer = x / y
        print("\nQuotient: " + str(answer))
    except ZeroDivisionError:
        print("\nError: Cannot divide by zero!")


done = False
while not done:
    print("================================")
    print("Welcome to the simple calculator!")
    print("Operations: add, sub, mult, div")
    print("Type \"done\" if done.")

    op = input("\nEnter operation: ").lower().strip()

    if op == "done":
        break

    if op not in ["add", "sub", "mult", "div"]:
        print("Invalid operation!")
        os.system('pause')
        os.system('cls')
        continue

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("\nInvalid input! Please enter numbers only.")
        os.system('pause')
        os.system('cls')
        continue

    if op == "add":
        add(num1, num2)
    elif op == "sub":
        sub(num1, num2)
    elif op == "mult":
        mult(num1, num2)
    elif op == "div":
        div(num1, num2)

    print("================================")
    os.system('pause')
    os.system('cls')
