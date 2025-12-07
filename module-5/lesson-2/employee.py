class Employee:
    def __init__(self,name,e_id,dept,sal):
        print("constructor called")
        self.name=name
        self.e_id=e_id
        self.dept=dept
        self.sal=sal
    def __del__(self):
        print("Destructor called")
    def intro(self):
        print(employee1.e_id)
        print(employee1.name)
        print(employee1.dept)
        print(employee1.sal)

employee1= Employee("rugved",101,"tech",80000000)
employee1.intro()
del employee1
employee1.intro()