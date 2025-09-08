def sum(num1, num2):
    return num1+num2
def sub(num1, num2):
    return num1-num2
def mul(num1, num2):
    return num1*num2
def div(num1, num2):
    return num1/num2
def fdiv(num1, num2):
    return num1//num2
def exp(num1, num2):
    return num1**num2
def mod(num1, num2):
    return num1%num2


num1=float(input(" Type num 1: "))
num2=float(input(" Type num 2: "))
operator=input(" Type operater: ")

if operator == "+":
    print (f"Answer of addition is {sum(num1,num2)}")
elif operator == "-" :
    print (f"Answer of subtraction is {sub(num1,num2)}")
elif operator == "*" :
    print (f"Answer of multiplication is {mul(num1,num2)}")
elif operator == "/" :
    print (f"Answer of diviaion is {div(num1,num2)}")
elif operator == "**" :
    print (f"Answer of exponentiation is {exp(num1,num2)}")
elif operator == "//" :
    print (f"Answer of floor division is {fdiv(num1,num2)}")
elif operator == "%" :
    print (f"Answer of modulus is {mod(num1,num2)}")
else:
    print ("Invalid")