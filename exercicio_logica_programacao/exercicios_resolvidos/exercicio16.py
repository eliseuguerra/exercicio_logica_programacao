def reverse_number_string(number):
    # Converts the number to a string
    number_string = str(number)

    # Reverses the string
    # The [::-1] is a slice that reverses the sequence
    reversed_number_string = number_string[::-1]

    # Converts the reversed string back to an integer
    reversed_number = int(reversed_number_string)

    return reversed_number

# Asks the user to enter a number
# We use int() to ensure the input is an integer
try:
    user_input = int(input("Enter a number to reverse: "))
    
    # Calls the function with the number provided by the user
    reversed_number = reverse_number_string(user_input)
    
    # Prints the result
    print(f"The original number is: {user_input}")
    print(f"The reversed number is: {reversed_number}")

except ValueError:
    print("Invalid input. Please enter only integer numbers.")