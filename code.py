import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

class TurtleCircle:
    def __init__(self, shape, color):
        self.turtle = trtl.Turtle(shape=shape)
        self.turtle.penup()
        self.turtle.color(color)
        self.turtle.pensize(2)

    def draw(self, startx, starty, startDir, forwardLength):
        self.turtle.goto(startx, starty)
        self.turtle.pendown()
        self.turtle.setheading(startDir)
        self.turtle.forward(forwardLength)
        self.turtle.right(45)

def main():
    startx = 0
    starty = 0
    startDir = 0
    forwardLength = 100

    for i in range(6):
        turtle_obj = TurtleCircle(turtle_shapes[i % len(turtle_shapes)], turtle_colors[i % len(turtle_colors)])
        turtle_obj.draw(startx, starty, startDir, forwardLength)
        startx, starty = turtle_obj.turtle.xcor(), turtle_obj.turtle.ycor()
        startDir += 45  

    wn = trtl.Screen()
    wn.mainloop()



if __name__ == "__main__":
    main()
