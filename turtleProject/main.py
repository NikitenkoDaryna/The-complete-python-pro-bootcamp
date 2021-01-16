import turtle as t
import random as r


def draw_figure(number_of_angles):
    for _ in range(0, number_of_angles):
        henry.forward(100)
        henry.right(360 / number_of_angles)


def draw_dashed_line(number_of_dashes):
    for _ in range(0, number_of_dashes):
        henry.pendown()
        henry.forward(10)
        henry.penup()
        henry.forward(10)


def generate_random_colour():
    red = r.randint(0, 255)
    green = r.randint(0, 255)
    blue = r.randint(0, 255)
    random_RGB = (red, green, blue)
    return random_RGB


def random_walk(step, number_of_steps):
    for s in range(number_of_steps):
        henry.color(generate_random_colour())
        henry.setheading(90 * r.randint(0, 3))
        henry.forward(step)

def draw_spirograph(step,radius):
    for x in range(int(360/step)):
        henry.color(generate_random_colour())
        henry.circle(radius)
        henry.setheading(henry.heading()+ x)

t.colormode(255)
henry = t.Turtle()
henry.shape("turtle")
henry.color("coral")
# for shape_size in range(3, 11):
#
#     draw_figure(shape_size)
# draw_dashed_line(10)

# henry.pensize(15)
# henry.speed("fastest")
# random_walk(30, 200)
# draw_figure(5)
henry.hideturtle()
henry.speed("fastest")
draw_spirograph(5,100)


screen = t.Screen()
screen.exitonclick()
