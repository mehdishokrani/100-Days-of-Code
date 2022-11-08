def add(number_1, number_2):
    """Add two numbers"""
    return number_1 + number_2

def subtraction(number_1, number_2):
    """Subtract two numbers"""
    return number_1 - number_2

def division(number_1, number_2):
    """This will divide two numbers"""
    return round(number_1 / number_2 , 2)

def multiplication(number_1 , number_2):
    """Multiply two numbers"""
    return number_1 * number_2
operations = {
    "+": add,
    "-": subtraction,
    "/": division,
    "*": multiplication
}

continue_to = True
while continue_to:
    first_number = float(input("Please enter the first number: "))
    second_number = float(input("Please enter the second number: "))
    for key in operations:
        print(f"{key}")
    
    operation_symbol = input("Pick an operation from lines above: ")
    if operation_symbol in operations:
        answer = operations[operation_symbol](first_number, second_number)
        print(f"{first_number} {operation_symbol} {second_number} = {answer}")
    else:
        print("It is a wrong operation that you chosen!!!")

    if input("Press 'Y' to comtinue or 'N' to stop calculator operations: ").lower() == "n":
        continue_to = False
        print("End of Calculations!!!")
    
