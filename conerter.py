while True:
    print("\n--- CONVERTER ---")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. KG to Pounds")
    print("4. KM to Miles")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        c = float(input("Enter Celsius: "))
        f = (c * 9/5) + 32
        print(f"{c}°C = {f}°F")

    elif choice == "2":
        f = float(input("Enter Fahrenheit: "))
        c = (f - 32) * 5/9
        print(f"{f}°F = {c}°C")

    elif choice == "3":
        kg = float(input("Enter KG: "))
        pounds = kg * 2.20462
        print(f"{kg} KG = {pounds} Pounds")

    elif choice == "4":
        km = float(input("Enter KM: "))
        miles = km * 0.621371
        print(f"{km} KM = {miles} Miles")

    elif choice == "5":
        print("Bye!")
        break

    else:
        print("Invalid choice")
