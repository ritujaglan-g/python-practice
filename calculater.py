
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Choose operation")
print("+  Addition")
print("-  Subtraction")
print("*  Multiplication")
print("/  Division")

op = input("Enter operation: ")

if op == "+":
    result = num1 + num2
    print("Result =", result)

elif op == "-":
    result = num1 - num2
    print("Result =", result)

elif op == "*":
    result = num1 * num2
    print("Result =", result)

elif op == "/":
    result = num1 / num2
    print("Result =", result)

else:
    print("Invalid operation")
