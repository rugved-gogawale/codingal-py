start=int(input("Enter start number"))
end=int(input("Enter end number"))
for i in range(start, end+1):
    if i%3==0 and i%5==0:
        # print("fizz buzz")
        continue
    elif i%5==0:
        print("buzz")
    elif i%3==0:
        print("fizz")
    else:
        print(i) 
