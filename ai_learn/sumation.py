#sumation code
def sumation(num1, num2):
    return num1 + num2
#subtraction code
def subtraction(num1, num2):
    return num1 - num2
#multiplication code
def multiplication(num1, num2):
    return num1 * num2
#division code
def division(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    return num1 / num2
print("Sumation of 5 and 3 is:", sumation(5, 3))
print("Subtraction of 5 and 3 is:", subtraction(5, 3))
print("Multiplication of 5 and 3 is:", multiplication(5, 3))
print("Division of 5 and 3 is:", division(5, 3))
