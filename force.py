print("Newton's second law of Motion")
print("--------------------------------------")
print("Select the missing value:")
print("1.Mass(m)")
print("2.Acceleration(a)")
print("3.Force(F)")
missing_value_choice = input("Enter the option number for the missing value: ")
if missing_value_choice == "1":
    a = float(input("Enter the acceleration (a): "))
    F = float(input("Enter the force (F): "))
    m = F / a
    print(f"Mass (m) = {m}")
elif missing_value_choice == "2":
    m = float(input("Enter mass (m): "))
    F = float(input("Enter Force (F):"))
    a = F / m
    print(f"Acceleration (a) = {a}")

elif missing_value_choice == "2":
    m = float(input("Enter mass (m): "))
    a = float(input("Enter Acceleration (a): "))
    F = m * a
    print(f"Force (F) = {F}")
else:
    print("Invalid option selected for the missing value.")