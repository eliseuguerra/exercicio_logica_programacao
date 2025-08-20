def withdraw_money(amount):
    """
    Calculates the optimal distribution of banknotes for a withdrawal.

    Args:
        amount (int): The integer value to be withdrawn.

    Returns:
        dict: A dictionary with the quantity of each banknote.
    """
    if amount <= 0:
        return {}

    notes = [100, 50, 20, 10, 5, 2, 1]
    distribution = {}

    for note in notes:
        if amount >= note:
            quantity = amount // note
            distribution[note] = quantity
            amount %= note

    return distribution

# --- Start of program execution ---

try:
    # Asks the user to enter the withdrawal amount
    withdrawal_amount_str = input("Enter the withdrawal amount (integer numbers only): ")
    withdrawal_amount = int(withdrawal_amount_str)

    # Calls the function to calculate the banknote distribution
    result = withdraw_money(withdrawal_amount)

    # Displays the result
    print(f"\nTo withdraw ${withdrawal_amount}, the banknote distribution is:")
    if result:
        for note, quantity in result.items():
            print(f"{quantity} note(s) of ${note}.00")
    else:
        print("No notes to be distributed. The amount must be greater than zero.")

except ValueError:
    print("Invalid input. Please enter an integer number only.")