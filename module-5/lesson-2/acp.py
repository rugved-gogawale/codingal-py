import turtle
import time 
class Circle:
    def __init__(self,radius):
        self.radius=radius

    def find_area (self):
        area=self.radius*self.radius*3.14159265359
        print(area)
    def find_circumfurence(self):
        circumfurence=self.radius*2*3.14159265359
        print(circumfurence)
           
    def draw_circle(self):
        turtle.circle(self.radius)
        turtle.done()
        # time.sleep(10)
      
circle1= Circle(int(input("enter the radius of your circle: ")))
#
circle1.draw_circle()
circle1.find_area()
circle1.find_circumfurence()