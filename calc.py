import os

def add(x, y):
    answer = x + y
    return print("\nSum: " + str(answer))

def sub(x, y):
    answer = x - y
    return print("\nDifference: " + str(answer))

def mult(x, y):
    answer = x * y
    return print("\nProduct: " + str(answer))

def div(x, y):
    answer = x / y
    return print("\nQuotient: " + str(answer))

done = False
while not done:
    print("================================")
    print("Welcome to the simple calculator!")
    print("Operations: add, sub, mult, div")
    print("Type \"done\" if done.")
    op = input("\nEnter operation: ")
    if op == "done":
        break
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if op == "add":
        add(num1, num2)
    elif op == "sub":
        sub(num1, num2)
    elif op == "mult":
        mult(num1, num2)
    elif op == "div":
        div(num1, num2)
    else:
        print("Invalid operation!")
    print("================================")

    os.system('pause')
    os.system('cls')
