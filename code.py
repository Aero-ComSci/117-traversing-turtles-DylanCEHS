#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

class Turtle:
  def __init__(self, shape, color):
    self.turtle = trtl.Turtle(shape=shape)
    self.turtle.penup
    self.turtle.color(color)
    self.turtle.pensize(2)
   
  def main(self, startx, starty, startDir, forwardLength):
        self.turtle.goto(startx, starty)
        self.turtle.pendown()
        self.turtle.setheading(startDir)
        self.turtle.right(45)
        self.turtle.forward(forwardLength)

my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  my_turtles.append(t)


startx = 0
starty = 0

for t in my_turtles:
  t.goto(startx, starty)
  t.right(45)     
  t.forward(50)

  startx = startx + 50
  starty = starty + 50

wn = trtl.Screen()
wn.mainloop()
