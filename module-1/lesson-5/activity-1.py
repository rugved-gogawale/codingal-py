def isLeapYear(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

year = int(input("Enter a year: "))

if isLeapYear(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")