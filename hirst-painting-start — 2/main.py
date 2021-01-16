###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
import turtle as t
import random as r

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     rgb_colors.append(color.rgb)
#
# print(rgb_colors)
henry = t.Turtle()

rgb_colours = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41),
               (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149),
               (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171),
               (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
               (176, 192, 208), (168, 99, 102)]


def draw_dotted_line(number_of_dashes, step, radius):
    for _ in range(0, number_of_dashes):
        henry.dot(radius, rgb_colours[r.randint(0, len(rgb_colours) - 1)])
        henry.penup()
        henry.forward(step)


def draw_picture(height, width, radius, step):
    for _ in range(0, height):
        draw_dotted_line(width, step, radius)
        henry.penup()
        henry.goto(henry.pos() + (-500, step))


t.colormode(255)
henry.penup()
henry.goto(-200, -200)
draw_picture(10, 10, 20, 50)
screen = t.Screen()
screen.exitonclick()
