import math

class Shape:
  def area(self):
    return 0

class Rectangle(Shape):
  def __init__(self,w,h):
    self.w=w
    self.h = h
  def area(self):
    return self.w*self.h

class Circle(Shape):
  def __init__(self,r):
    self.r=r
  def area(self):
    return math.pi*self.r*self.r

user_input = input().split()
shape_type = user_input[0]

if shape_type == "Rectangle":
  w = int(user_input[1])
  h = int(user_input[2])
  shape = Rectangle(w,h)
  area = shape.area()
  print(f"Area : {area:.2f}")
  
elif shape_type == "Circle":
  r = int(user_input[1])
  shape = Circle(r)
  rea = shape.area()
  print(f"Area : {area:.2f}")
else :
  print("Invalid")