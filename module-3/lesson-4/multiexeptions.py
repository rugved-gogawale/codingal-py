num1=int(input("Enter a number"))
num2=int(input("Enter a number"))
try:
   
    result= num1/num2
    print("Result is : ", result)
    print("Result is : ", result1)
except ZeroDivisionError:
    print("Division by 0 is not allowed")
except ValueError:
    print("Please enter the numerical value")
except NameError as ex:
    print("the exeption is", ex)
except:
    print("some error occured")
finally:
    print("I will execute no matter what")