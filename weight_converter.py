weight = int(input('Enter your weight: '))
unit = input("Enter unit 'L' (pounds) or 'K' (kilogram): ")
if unit.upper() == "L":
    converted = weight * 0.45
    print(f'Your weight: {converted} kilograms')
elif unit.upper() == "K":
    print(f'Your Weight: {weight / 0.454} pounds')
else:
    print("Please enter valid unit.")
