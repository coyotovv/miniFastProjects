firstNum = input ("Enter first number: ")
secondNum = input("Enter second number: ")
arithmetic = input("Enter operation (+, -, *, /): ")

if arithmetic == '+':
    result = float(firstNum) + float(secondNum)
elif arithmetic == '-':
    result = float(firstNum) - float(secondNum)
elif arithmetic == '*':
    result = float(firstNum) * float(secondNum)
elif arithmetic == '/':
    if float(secondNum) != 0:
        result = float(firstNum) / float(secondNum)
    else:
        result = "Error: Division by zero"

else:
    result = "Error: Invalid operation"


print(f"The result is: {result}")