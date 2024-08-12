import random
import turtle as t
import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.png', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

t.colormode(255)
timmy = t.Turtle()
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()
color_list = [(203, 165, 108), (152, 74, 48), (52, 93, 124), (170, 153, 41), (223, 202, 136), (137, 32, 21), (132, 163, 185), (47, 121, 88), (198, 91, 72), (15, 99, 73), (70, 47, 39), (147, 179, 148), (98, 73, 75), (162, 142, 157), (234, 175, 164), (55, 46, 49), (184, 205, 172), (24, 81, 87), (38, 61, 74), (142, 22, 25), (85, 146, 126), (45, 65, 85), (175, 91, 94), (214, 177, 183), (18, 70, 64), (109, 125, 151)]

timmy.setheading(225)
timmy.forward(350)
timmy.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots+1):
    timmy.dot(20, random.choice(color_list))
    timmy.setheading(0)
    timmy.forward(50)

    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)



screen = t.Screen()
screen.exitonclick()

