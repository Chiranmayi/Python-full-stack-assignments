class Circle:
    def area(self, radius):
        return 3.14 * radius * radius


class Rectangle:
    def area(self, length, width):
        return length * width


circle = Circle()
rectangle = Rectangle()

radius = float(input("Enter radius: "))
length = float(input("Enter length: "))
width = float(input("Enter width: "))

print("Circle Area:", circle.area(radius))
print("Rectangle Area:", rectangle.area(length, width))