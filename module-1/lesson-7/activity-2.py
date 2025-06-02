m1=float(input("enter your marks for test 1 : "))
m2=float(input("enter your marks for test 2 : "))
m3=float(input("enter your marks for test 3 : "))
average = (m1 + m2 + m3) / 3  
print(f"Your average is = {average}")
if average > 69:
    print("Your grade is A")
elif average > 59:
    print("Your grade is B")
    
elif average > 49:
    print("Your grade is C")
  
elif average > 39:
    print("Your grade is D")
else:
    print("Your grade is E")


