try:
    num1=int(input("Enter a your age: "))
    if num1 % 2 == 0:
        print("Your age is even")
    else:
        print("Your age is odd")
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