class circle :
    pi=3.14
    def __init__(self,rad) :
        self.rad = rad
    def area (self) :
        c= circle.pi *(self.rad**2)
        return c
r=int(input("enter the radiii:"))
c=circle(r)
print("the area=",c.area())

'''r=int(input("enter the radius:"))
pi=22/7
c=pi*(r**2)
print("the area of the circle is:",c)'''

'''
class Circle:
    pi = 3.14

    def __init__(self, rad):
        self.rad = rad

    def area(self):
        return Circle.pi * (self.rad ** 2)

r = int(input("Enter the radius: "))
c = Circle(r)
print("The area =", c.area())
'''