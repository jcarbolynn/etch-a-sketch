from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
  tim.forward(10)

def move_backwards():
  tim.backward(10)

def turn_clockwise():
  tim.right(10)

def turn_counterclockwise():
  tim.left(10)


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=turn_clockwise)
screen.onkey(key="a", fun=turn_counterclockwise)
screen.onkey(key="space", fun=tim.clear)
screen.exitonclick()
