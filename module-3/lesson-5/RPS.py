import random
options=["Rock", "Paper", "Scissors"]
user= input("Choose 'Rock', 'Paper' or 'Scissors'")
option=random.choice(options)
print(f"you chose : {user}")
print(f"Computer chose : {option}")

if user == option:
    print("Its a tie")
elif user == "Rock" and option == "Scissors":
    print("You won")
elif user == "Scissors" and option == "Paper":
    print("You won")
elif user == "Paper" and option == "Rock":
    print("You won")
else:
    print("You lose")