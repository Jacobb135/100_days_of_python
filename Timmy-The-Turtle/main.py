import turtle
from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return timmy_the_turtle.color(r, g, b)


timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("green")
timmy_the_turtle.speed("fastest")



for _ in range(200):
    timmy_the_turtle.circle(100)
    random_color()
    timmy_the_turtle.setheading(timmy_the_turtle.heading() + 10)



screen = Screen()
screen.exitonclick()
