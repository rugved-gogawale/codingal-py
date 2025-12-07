
class dog:


    species = "dog"


    def __init__(self, name, age):
        self.name = name
        self.age = age

blu = dog("dog", 10)
woo = dog("dog2", 15)


print("Blu is a {}".format(blu.species))
print("Woo is also a {}".format(woo.species))


print("{} is {} years old".format( blu.name, blu.age))
print("{} is {} years old".format( woo.name, woo.age))