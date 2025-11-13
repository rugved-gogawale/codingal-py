def cube(n):
    return n*n*n
number=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
cubelist=list(map(cube,number))
print(cubelist)
zipped=list(zip(number,cubelist))
print(zipped)