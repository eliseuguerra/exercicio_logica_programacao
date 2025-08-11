while True:
    try:
        number = int(input("Please enter an integer less than 32: "))

        if 0 <= number < 32:
            binary_representation = bin(number)[2:]
            print(f"The binary representation of {number} is {binary_representation}")
            break  # Exit the loop if the number is valid
        else:
            print("Invalid number! Please enter a number between 0 and 31.")

    except ValueError:
        print("Invalid input! Please enter only integers.")