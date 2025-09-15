def find_cube(n):
    return n*n*n
def is_even(n):
    if n%2==0:
        return find_cube(n)
    else:
        return "Enter a even number. "
n=int(input("Enter a number : "))
print(is_even(n))