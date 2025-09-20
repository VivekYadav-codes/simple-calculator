# simple calculator
def add(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiply(x, y):
    return x * y

def division(x, y):
    if y == 0:
        return "Error: Division by zero"
    else:
        return x / y

print("=== Simple Calculator ===")
print("Choose operation:")
print("1. Add (+)")
print("2. Subtraction (-)")
print("3. Multiply (*)")
print("4. Division (/)")

op = input("Enter your choice (+, -, *, /): ")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if op == '+':
    result = add(a, b)
elif op == '-':
    result = subtraction(a, b)
elif op == '*':
    result = multiply(a, b)
elif op == '/':
    result = division(a, b)
else:
    result = "Invalid operator"

print("Result:", result)
