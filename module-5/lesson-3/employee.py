class Person:
    def __init__(self,name, age, city):
        self.name=name
        self.age=age
        self.city=city
class Employee(Person):
    def __init__(self, name, age, city, salary, post):
        super().__init__(name, age, city)
        self.salary=salary
        self.post=post
    def display (self):
        print(self.name, self.age, self.city, self.salary, self.post)
employee1=Employee("bob",1000,"london",-2000,"ceo")
employee1.display()
employee2=Employee("john",1,"new york",2000,"worker")
employee2.display()