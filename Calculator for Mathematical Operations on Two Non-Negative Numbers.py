#Developer Name: Nicole Adrianne M. Esmeralda
#Date of Development: September 3, 2023

# Define a function that performs mathematical operations based on the input operation
def program3(x, y, operation):
    if operation == 'A': # Addition
        return x + y
    elif operation == 'S': # Subtraction
        return x - y
    elif operation == 'M': # Multiplication
        return x * y
    elif operation == 'D': # Division
        if y != 0: # Checking for zero divisor
            return x / y
        else:
            return "Division by zero is undefined."
    elif operation == 'R': # Remainder
        if y != 0: # Checking for zero divisor
            return x % y
        else:
            return "Can't find remainder with zero divisor."

# Display a menu of available mathematical operations
print("""Please choose a mathematical operation by entering the corresponding letter: 
A: Addition
S: Subtraction
M: Multiplication
D: Division
R: Remainder""")

# Get user input and convert it to uppercase for case insensitivity
select_operation = input("Enter chosen operation: ").upper()

# Check if the selected operation is valid
if select_operation not in ['A', 'S', 'M', 'D', 'R']:
    print("Invalid selected operation. Please choose from the available options")
else:
    # Get user input for the two non-negative numbers
    first_number = float(input("Enter the first non-negative number: "))
    second_number = float(input("Enter the second non-negative number: "))

    # Check if the entered numbers are non-negative
    if first_number < 0 or second_number < 0:
        print("Invalid input. Both numbers must be non-negative")
    else:
        # Call the program3 function and display the result
        result = program3(first_number, second_number, select_operation)
        print("Result:", result)
