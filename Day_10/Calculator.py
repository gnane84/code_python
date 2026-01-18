# TODO: Write out the math function - Add, subtract, multiply and divide.
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# TODO: Add these function into a dictionary as the values. Keys = "+", "-", "*", "/"

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

#TODO: calculator_function
def calculator():
    should_accumulate = True
    num1 = int(input("Enter first number: "))
    while should_accumulate:
        for operation in operations:
            print(operation)
        operation_symbol = input("Enter operation: ")
        num2 = int(input("Enter second number: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        choice = input(f"Type 'y' to continue calculation with {answer}?, or type 'n' to start new calculation: ")
        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()




