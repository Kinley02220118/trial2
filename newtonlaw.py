print("newton law of motion")
print("......")

#determine the missing value
print("selectt the missing value")
print("1.mass(m):")
print("2.acceleration(a):")
print("3.force(f):")
missing_value=input("enetr the option number for the missing value:")

if missing_value=="1":
    a=float(input("enter acceleration(a)"))
    f=float(input("enetr force(f):"))
    m=f/a
    print(f'mass(a)={m}')

elif missing_value=="2":
    m=float(input("enter mass:"))
    f=float(input("enetr force:"))
    a=f/m
    print(f'accelerartion(f)={a}')
elif missing_value=="3":
    m=float(input("enter mass:"))
    a=float(input("enter acceleration:"))
    f=m*a
    print(f'force(a)={f}')

else:
    print("invalid")