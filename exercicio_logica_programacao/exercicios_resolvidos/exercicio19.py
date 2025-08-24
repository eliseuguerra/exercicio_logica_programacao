a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))

if a == 0:
    if b == 0:
        print("The equation has infinite solutions.")
    else:
        print("The equation has no solution.")
else:
    x = -b / a
    print(f"The root of the equation is: {x}")

