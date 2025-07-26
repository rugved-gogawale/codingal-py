start=int(input("enter start number: "))
stop=int(input("enter stop number: "))
stop= stop+1
sum=0
for i in range(start,stop):
    print(i)
    sum+=i
print(f"The sum was : {sum}")
print("Numbers are in reverse order")
for i in range(stop-1,start-1,-2):
    print(i)
