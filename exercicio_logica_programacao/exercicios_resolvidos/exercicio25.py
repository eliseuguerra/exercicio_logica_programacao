import calendar

try:
    # Prompt the user for the month number and the year
    month_num = int(input("Enter the month number (1-12): "))
    year = int(input("Enter the year: "))

    # Check if the month number and year are valid
    if 1 <= month_num <= 12 and year > 0:
        # Use the monthrange function from the calendar library to get the number of days
        # monthrange returns a tuple: (weekday of the 1st day, number of days in the month)
        days = calendar.monthrange(year, month_num)[1]
        
        # Print the result
        print(f"The month {month_num} of the year {year} has {days} days.")
    else:
        print("Invalid input. Please enter a month number between 1 and 12 and a valid year.")

except ValueError:
    print("Invalid input. Please enter integer numbers only.")
