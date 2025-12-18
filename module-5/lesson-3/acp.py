class Vehicle:
    def __init__(self,size):
        self.size=size
    def fare(self):
        return self.size*100
    def display_fare(self):
        print(f"The fare is {self.fare()}")    
        
class Bus(Vehicle):
    def __init__(self,size):
        super().__init__(size)
    def fare(self):
        return (self.size*100)*1.1    
    def display_fare(self):
        print(f"The fare is {self.fare()}")
vehicle1=Vehicle(1234566789123456789123456789123456789)
vehicle1.display_fare()
bus1=Bus(1234566789123456789123456789123456789)
bus1.display_fare()
