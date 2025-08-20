height_person = float(input("Enter your height in meters: "))
shadow_person = float(input("Enter the length of your shadow in meters: "))
shadow_building = float(input("Enter the length of the building's shadow in meters: "))

if shadow_person == 0:
    print("Error: The length of your shadow cannot be zero.")
else:
    height_building = (height_person * shadow_building) / shadow_person
    print(f"\nThe height of the building is approximately {height_building:.2f} meters.")