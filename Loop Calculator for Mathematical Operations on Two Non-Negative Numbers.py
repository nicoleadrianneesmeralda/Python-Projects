#Developer Name: Nicole Adrianne M. Esmeralda
#Date of Development: September 3, 2023

# Infinite loop to repeatedly prompt the user for mathematical operations
while True:
    print("""Please choose a mathematical operation by entering the corresponding number:
    1: Addition
    2: Subtraction
    3: Multiplication
    4: Division
    5: Modulus Division
    6: Exponent
    7: Floor Division
    Press 'x' to exit""")

   # Get user input and convert it to lowercase for case insensitivity of 'x' for program exit
    user_input = input("Enter chosen operation: ").lower()

    # Exit the program if the user inputs 'x'
    if user_input == 'x':
        print("Exiting the program.")
        break

    # Check if the user input is valid (1 to 7)
    if user_input not in ['1', '2', '3', '4', '5', '6', '7']:
        print("Invalid selected operation. Please choose from the available options.")
        continue

    # Get the two non-negative integers from the user
    first_num = int(input("Enter the first non-negative integer: "))
    second_num = int(input("Enter the second non-negative integer: "))

    # Check if the input numbers are non-negative
    if first_num < 0 or second_num < 0:
        print("Invalid input. Both numbers should be non-negative.")
        continue

    # Perform the selected mathematical operation
    if user_input == '1':
        result = first_num + second_num
    elif user_input == '2':
        result = first_num - second_num
    elif user_input == '3':
        result = first_num * second_num
    elif user_input == '4':
        if second_num == 0:
            print("Error: Division by zero is undefined.")
            continue
        result = first_num / second_num
    elif user_input == '5':
        if second_num == 0:
            print("Error: Modulus division by zero is undefined.")
            continue
        result = first_num % second_num
    elif user_input == '6':
        result = first_num ** second_num
    elif user_input == '7':
        if second_num == 0:
            print("Error: Floor division by zero is undefined.")
            continue
        result = first_num // second_num

    # Display the result of the operation
    print("Result:", result)