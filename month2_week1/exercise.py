from abc import ABC, abstractclassmethod

class Rectangle:
    def __init__(self,length, width):
        self.length = length
        self.width = width
        self.__color="green"
        

    def calcArea(self):
        return self.length * self.width
    
    def calcPerimeter(self):
        return 2*(self.length+self.width)
    

# rect=Rectangle(10.43,6.4)
# print(rect.calcArea())
# print(rect.calcPerimeter())
# print(rect.__color)

class Shape:
    def __init__(self,color):
        pass

    def get_color(self):
        pass

    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self,color,width,length):
        self.width = width
        self.color =color
        self.length=length

    def get_color(self):
        return self.color
        
    def area(self):
        return self.length * self.width
    

class Circle(Shape):
    def __init__(self,color,radius):
        self.color =color
        self.radius=radius

    def get_color(self):
        return self.color
        
    def area(self):
        return round(2*3.1415*self.radius,2)
    
# class DisplayInfo(Shape):
#     print(Shape.get_color())
#     print(Shape.area())
#     print()


circle=Circle("green",5)
print(circle.get_color())
print(circle.area())
print()

rectangle=Rectangle("red",10,5)
print(rectangle.__color)
print(rectangle.area())
print()

# DisplayInfo(Circle("green",5))


