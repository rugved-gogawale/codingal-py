buying=float(input("enter the buying price: "))
selling=float(input("enter the selling price: "))
if selling > buying:
    print(f"Profit = {selling-buying}")
elif selling < buying:
    print(f"Loss = {buying-selling}")
else:
    print("No Profit No Loss = 0 ")