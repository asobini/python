

from sqlalchemy.testing.util import random_choices

###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##

#import colorgram

#colors = colorgram.extract('image.jpg', 30)

#col_palette = []

#for color in colors: # looping through a list of objects 'color"
#     r = color.rgb.r  #saving each objects rbg value of red into variable "r"
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb = (r,g,b)         #creating color tuples
#     col_palette.append(rgb) #creating a list of color (rgb) tuples

#print(col_palette)
import turtle as turtle_module
import random

color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]


t = turtle_module.Turtle()
t.penup()
screen = turtle_module.Screen()
t.hideturtle()

screen.colormode(255) ## set colormode on screen to rgb values
screen.screensize(650, 650)

dotsize = 20
space = 50

start_x = -screen.window_width() // 2 + 50  # Add margin from the edge
start_y = -screen.window_height() // 2 + 50  # Add margin from the edge
t.goto(start_x, start_y)

for y in range(1,11):
    for _ in range(1,11):
        t.dot(20, random.choice(color_list))
        t.penup()
        t.forward(50)
    start_y +=50
    t.goto(start_x, start_y)

screen.exitonclick()


