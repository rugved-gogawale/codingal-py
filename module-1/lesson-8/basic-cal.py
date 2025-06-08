num1=float(input(" Type num 1"))
num2=float(input(" Type num 2"))
operator=input(" Type operater")
if operator == "+" :
    print (f"Answer of addition is {num1 + num2}")
elif operator == "-" :
    print (f"Answer of subtraction is {num1 - num2}")
elif operator == "*" :
    print (f"Answer of multiplication is {num1 * num2}")
elif operator == "/" :
    print (f"Answer of diviaion is {num1 / num2}")
elif operator == "**" :
    print (f"Answer of exponentiation is {num1 ** num2}")
elif operator == "//" :
    print (f"Answer of floor division is {num1 // num2}")
elif operator == "%" :
    print (f"Answer of modulus is {num1 % num2}")
else:
    print ("Invalid")