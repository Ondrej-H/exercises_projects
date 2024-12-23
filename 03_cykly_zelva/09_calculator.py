
def calculate(num1, operation, num2):
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2
    else:
        result = "I don't understand that."
    return result


first_number = int(input("First number: "))
operation = input("Operation: ")
second_number = int(input("Second number: "))

print(f"{first_number} {operation} {second_number} = {calculate(first_number, operation, second_number)}")
