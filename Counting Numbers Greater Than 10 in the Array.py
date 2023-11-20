# Developer name: Nicole Adrianne M. Esmeralda
# Date of development: September 17, 2023

# Initialize an empty list to store numbers
numbers = []

# Get the size of the array from the user
array_size = int(input("Enter the size of the array: "))

# Loop through the specified array size to assign an element number to each input element.
for i in range(array_size):
    # Prompt the user to enter an element and convert it to a float
    element = float(input(f"Enter element {i+1}: "))
    # Append the entered element to the 'numbers' list
    numbers.append(element)

# Initialize a count variable to count the elements greater than 10
count = 0
# Loop through each element in the 'numbers' list
for element in numbers:
    # Check if the current element is greater than 10
    if element > 10:
        count += 1 # Increment the count if the condition is met

# Print the array elements
print(f"Array elements = {numbers}")
# Print the number of elements larger than 10 in the array
print(f"Number of elements larger than 10 in the array = {count}")