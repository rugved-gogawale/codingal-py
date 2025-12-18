class Product:
    __price=-0
    def __init__(self,exp,size,quantity):
        self.exp=exp
        self.size=size
        self.quantity= quantity
    def display(self):
        print(self.exp,self.size,self.quantity)
        
p1=Product("20/12/1796", -8,100)
p1.display()
print(p1.__price)

    


