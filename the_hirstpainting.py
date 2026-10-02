
from turtle import Turtle,Screen
tim = Turtle()
import random
screen = Screen()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
screen.colormode(255)




color_list = [(229, 228, 225), (227, 223, 225), (198, 174, 118), (215, 225, 218), (222, 225, 230), (126, 36, 24), (162, 103, 57), (185, 158, 52), (6, 55, 82), (46, 34, 31), (108, 68, 85), (115, 161, 174), (22, 120, 171), (67, 152, 135), (75, 37, 47), (9, 66, 46), (88, 139, 59), (128, 39, 42), (181, 97, 80), (209, 201, 148), (142, 176, 161), (176, 156, 161), (179, 202, 183), (218, 179, 171), (31, 78, 61), (86, 142, 154), (21, 77, 98), (169, 200, 207), (149, 115, 121), (207, 181, 187)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

number_of_dots = 100

for dot_count in range(1,number_of_dots + 1):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.left(90)
        tim.forward(50)
        tim.left(90)
        tim.forward(500)
        tim.setheading(0)
screen.exitonclick()