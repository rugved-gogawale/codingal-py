sunny = 0
rain = 0
weather_tuple=[]
for i in range(0,7):
    weather = input("Enter the weather in (r) for rain and (s) for sunny ")
    weather_tuple.append(weather)
print(weather_tuple)
for i in range(0,7):
    if weather_tuple[i]=="s":
        sunny+=1
    else:
        rain+=1
if sunny > rain:
    print("Good weather")
else:
    print("Bad weather")