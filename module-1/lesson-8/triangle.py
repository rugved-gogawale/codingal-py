side1=float(input("Enter side 1: "))
side2=float(input("Enter side 2: "))
side3=float(input("Enter side 3: "))
if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    print("It is a valid triangle")
    if side1 == side2 and side3 == side1:
        print("The triangle you inputed is an equilatral triangle")
    elif side1 == side2 or side2 == side3 or side1 == side3:
        print("This is and isoceles triangle")
    else:
        print("This is a scalene triangle")
else:
    print("It is a invalid triangle")