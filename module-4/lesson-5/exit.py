number=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
for i in number:
    if i % 4 == 0:
        print(f"{i} Not allowed ")
        exit()
    else:
        print(f"{i} Allowed")

    