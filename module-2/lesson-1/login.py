username=input("Enter your name  : ")
if username.lower() == "rugved":
    print(f"The username {username} is correct")
    password=input("Enter the password")
    if password=="abc":
        print("login succesfull")
    else:
        print("incorrect password")
else:
    print("incorrect username")