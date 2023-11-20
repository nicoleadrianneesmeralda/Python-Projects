#Developer Name: Nicole Adrianne M. Esmeralda
#Date of Development: October 16, 2023

# Function to create a new stack
def create_stack(name): # 'name' parameter is the name of the stack to be created
    stack = list() # Create an empty list to represent the stack
    print(f"Stack '{name}' created successfully.") # Print a message confirming the successful creation of the stack with the given name
    return stack # Return the created stack

def isempty(stack): # Function to check if a stack is empty
    return len(stack) == 0 # Returns True if the stack is empty, otherwise returns False

# Function to add an element to the stack
def push(stack, n, name): # 'name' parameter is the name of the stack, 'n' parameter is the element to be pushed onto the stack
    stack.append(n) # Add the given element to the stack
    print(f"Pushed element: {n}") # Prints the element that was pushed onto the stack
    show(stack, name) # Call the 'show' function to display the elements in the stack

# Function to remove the top element from the stack
def pop(stack, name): # 'name' parameter is the name of the stack from which the item will be popped
    if isempty(stack): # Check if the stack is empty
        print("Stack is empty") # Print a message indicating that the stack is empty
    else: #If stack is not empty
        print(f"Popped item: {stack.pop()}") # Print the item that was removed from the stack
        show(stack, name) # Call the 'show' function to display the elements in the stack

# Function to display all elements in the stack
def show(stack, name): # 'name' parameter is the name of the stack to be displayed
    print(f"Elements of the '{name}' stack: ") # Print a message indicating the elements of the stack are about to be displayed
    for i in stack: # Iterate over each element in the stack
        print(i) # Print each element in the stack

# Function to display the top element of the stack without removing it
def peek(stack, name): # 'name' parameter is the name of the stack to peek at
    if isempty(stack): # Check if the stack is empty
        print("Stack is empty") # Print a message indicating that the stack is empty
    else: #If stack is not empty
        print(f"Top element: {stack[-1]}") # Print the top element of the stack
        show(stack, name) # Call the 'show' function to display the elements in the stack

def main(): # Main function to execute stack operations based on user input
    stack = None # Initializes the stack as 'None'
    while True: # Execute an infinite loop
        print("""Choose a stack operation by entering the corresponding letter:
        [C] - Create a stack 
        [A] - Append element to stack
        [D] - Remove element on stack
        [P] - Peek the top element of the stack
        [S] - Show the stack elements
        Press 'x' to exit""") # Print the stack operations for the user to choose from

        choice = input("Enter your chosen stack operation: ").upper()  # Take user input and convert it to uppercase

        # Perform respective operations based on the user's input
        if choice == 'C': # Check if the choice is to create a stack
            stack_name = input("Enter stack name: ") # Take input for the name of the stack
            stack = create_stack(stack_name) # Call the 'create_stack' function to create a new stack

        elif choice == 'A': # Check if the choice is to append an element to the stack
            if stack is None: # Check if no stack has been created yet
                print("Please create a stack first.") # Print a message if the stack has not been created yet
            else: # If the stack has been created
                element = input("Enter element to append: ") # Takes input for the element to be added to the stack
                push(stack, element, stack_name) # Calls the 'push' function to add the element to the stack

        elif choice == 'D': # Check if the choice is to remove an element from the stack
            if stack is None: # Check if no stack has been created yet
                print("Please create a stack first.") # Prints a message if the stack has not been created yet
            else: # If the stack has been created
                pop(stack, stack_name) # Calls the 'pop' function to remove the top element from the stack

        elif choice == 'P': # Check if the choice is to peek the top element of the stack
            if stack is None: # Check if no stack has been created yet
                print("Please create a stack first.") # Prints a message if the stack has not been created yet
            else: # If the stack has been created
                peek(stack, stack_name) # Call the 'peek' function to display the top element of the stack

        elif choice == 'S': # Check if the choice is to show all elements in the stack
            if stack is None: # Check if no stack has been created yet
                print("Please create a stack first.") # Prints a message if the stack has not been created yet
            else: # If the stack has been created
                show(stack, stack_name) # Call the 'show' function to display all elements in the stack

        elif choice == 'X': # Check if the choice is to exit the program
            print("Exiting the program...") # Print a message indicating that the program is being exited
            break # Exits the program

        else: # If entered operation is invalid
            print("Invalid operation. Please choose from the available options.") # Print a message for invalid input

if __name__ == "__main__": # Check if the script is being run as the main program
    main() # Call the 'main' function if the script is executed directly