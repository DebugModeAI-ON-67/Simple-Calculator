def add(x, y):
    answer = x + y
    return print(answer)

def sub(x, y):
    answer = x - y
    return print(answer)

def mult(x, y):
    answer = x * y
    return print(answer)

def div(x, y):
    answer = x / y
    return print(answer)

done = False
while not done:
    print("Operations: add, sub, mult, div")
    print("Type \"done\" if done.")
    op = input("Enter operation: ")
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
    elif op == "done":
        done = True
