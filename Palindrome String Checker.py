# Developer name: Nicole Adrianne M. Esmeralda
# Date of development: September 17, 2023

# Define a function to check if a string is a palindrome
def palindrome(input_string):
    # Remove spaces and convert the input string to lowercase
    remove_spaces = input_string.replace(" ", "").lower()

    # Initialize an empty list to store characters
    character_array = []

    # Loop through each character in the cleaned string stored in the 'remove_spaces' variable
    for character in remove_spaces:
        # Append the character to the character_array
        character_array.append(character)

    # Create a reversed version of the character_array
    reversed_array = character_array[::-1]

    # Check if the original and reversed arrays are the same
    if character_array == reversed_array:
        return True # The string is a palindrome
    else:
        return False # The string is not a palindrome

# Get user input for a string
user_input = input("Enter a string: ")

# Call the palindrome function and check if the input is a palindrome
if palindrome(user_input):
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")