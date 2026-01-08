"""""""""Create a Python program that defines an abstract class called Payment with an abstract method process_payment to demonstrate abstraction. Implement polymorphism by creating two subclasses, CreditCard and PayPal, that each provide their own unique logic for the payment method. Finally, create a list containing instances of both classes and use a loop to process a payment of 100 for each"""""""""

from abc import ABC,abstractmethod

class Payment(ABC):
    def __init__(self, amount):
        
        self.amount=amount
    def process_payment(self):
        pass
class CreditCard(Payment):
    def __init__(self, amount):

        self.amount=amount
    def process_payment(self):
        print("Payment was done using credit card")
class PayPal(Payment):
    def __init__(self, amount):

        self.amount=amount
    def process_payment(self):
        print("Payment was done using paypal")

p1=Payment(200)
p1.process_payment()

p3=CreditCard(100)
p3.process_payment()

p2=PayPal(250)
p2.process_payment()
    
