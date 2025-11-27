import random
number=random.randint(1,20)
guess=int(input("Enter your guess for the number which is between 1-20"))
count=0
if number== guess:
    print("You have solved")
else:
    print("wrong answer try again")
    while count < 4:
        if number>guess:
            print("Too low")
            guess=int(input("Enter your guess for the number which is between 1-20"))
        elif number>guess:
            print("too high")
            guess=int(input("Enter your guess for the number which is between 1-20"))
            count+=1
        else:
            print("")