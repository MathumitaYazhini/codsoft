def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    print("Unique Python Calculator 🧮")
    print("Operations: + (Add), - (Subtract), * (Multiply), / (Divide)")

    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }

    try:
        a = float(input("Enter the first number: "))
        op = input("Enter operation (+, -, *, /): ").strip()
        b = float(input("Enter the second number: "))

        if op in operations:
            result = operations[op](a, b)
            print(f"Result: {a} {op} {b} = {result}")
        else:
            print("Unsupported operation! Please use one of: +, -, *, /")

    except ValueError:
        print("Invalid input. Please enter numerical values only.")

if __name__ == "__main__":
    calculator()
