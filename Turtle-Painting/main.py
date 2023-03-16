import turtle
from turtle import Turtle, Screen
color_list = [(203, 157, 117), (58, 96, 133), (153, 84, 54), (220, 209, 118), (135, 163, 189), (21, 37, 58), (189, 145, 159), (125, 73, 93), (49, 28, 18), (131, 178, 154), (178, 162, 37), (56, 121, 75), (197, 95, 77), (56, 28, 38), (149, 24, 15), (127, 28, 42), (21, 47, 39), (185, 95, 112), (227, 169, 188), (226, 176, 166), (60, 164, 104), (40, 61, 100), (108, 120, 167), (157, 210, 184), (22, 93, 56), (177, 186, 214)]
timmy = Turtle()
turtle.colormode(255)
counter = 0
row_counter = 0
timmy.speed("slowest")
timmy.shape("turtle")
for _ in range(100):
    if counter >= len(color_list):
        counter = 0
    timmy.color(color_list[counter])
    timmy.begin_fill()
    timmy.circle(25)
    timmy.end_fill()
    timmy.penup()
    timmy.forward(35)
    timmy.pendown()
    counter += 1
    row_counter += 1
    if row_counter % 10 == 0:
        timmy.penup()
        timmy.back(350)
        timmy.left(90)
        timmy.forward(35)
        timmy.right(90)
        row_counter = 0

my_screen = Screen()
my_screen.exitonclick()