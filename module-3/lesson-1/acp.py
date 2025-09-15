pi=3.14159265359
def cir(rad):
    return rad*pi*2
def area(rad):
    return rad * rad * pi
rad=int(input("Enter the radius:"))
print(cir(rad),area(rad))