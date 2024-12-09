from random import randint
import turtle



# class Point
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if (
            rectangle.lowleft.x < self.x < rectangle.upright.x
            and rectangle.lowleft.y < self.y < rectangle.upright.y
        ):
            return True
        else:
            return False

    def distance_from_point(self, point):
        return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5


# class Rectangle
class Rectangle:
    def __init__(self, lowleft, upright):
        self.lowleft = lowleft
        self.upright = upright

    def rect_area(self):
        return (self.upright.x - self.lowleft.x) * (self.upright.y - self.lowleft.y)

#Class GuiRectangle
class GuiRectangle(Rectangle):
    def draw(self,user_point_x,user_point_y):
        myturtle = turtle.Turtle()
        myturtle.penup()
        myturtle.goto(self.lowleft.x, self.lowleft.y)
        myturtle.pendown()
        myturtle.forward(self.upright.x - self.lowleft.x)
        myturtle.left(90)
        myturtle.forward(self.upright.y - self.lowleft.y)
        myturtle.left(90)
        myturtle.forward(self.upright.x - self.lowleft.x)
        myturtle.left(90)
        myturtle.forward(self.upright.y - self.lowleft.y)
        myturtle.penup()
        myturtle.goto(user_point_x,user_point_y)
        turtle.done()


rectangle = Rectangle(
    Point(randint(0, 400), randint(0, 400)), Point(randint(10, 400), randint(10, 400))
)


user_point = Point(float(input("Guess X:")), float(input("Guess Y:")))
user_area = float(input("Guess the are :"))



print("Your point was inside rectangle:", user_point.falls_in_rectangle(rectangle))
print(
    "Rectangle Coordinates:",
    rectangle.lowleft.x,
    ",",
    rectangle.lowleft.y,
    "and",
    rectangle.upright.x,
    ",",
    rectangle.upright.y,
)

print("ur guess of rectangle area is off by:", rectangle.rect_area() - user_area)
print("Rectagle are is :", rectangle.rect_area())

GuiRectangle.draw(rectangle,user_point.x,user_point.y)
