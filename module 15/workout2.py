pi = 3.14 

class Circle:

    def __init__(self,radius):
        self.radius = radius
    
    def get_area(self):
        return pi * self.radius ** 2
    
    def get_circumference(self):
        return 2 * pi * self.radius

# Example usage

radius = float(input("Enter the radius of the circle: "))
circle = Circle(radius)

area = circle.get_area()
circumference = circle.get_circumference()

print("The area of the circle is:", area)

print("The circumference of the circle is:", circumference)