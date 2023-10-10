###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
#import colorgram
#
#rgb_colors = []
#colors = colorgram.extract('image.jpg', 30)
#for color in colors:
#    r=color.rgb.r
#    g=color.rgb.g
#    b=color.rgb.b
#    new_color=(r,g,b)
#    rgb_colors.append(new_color)
#
#print(rgb_colors)

import turtle as turtle_module
import random
tim=turtle_module.colormode(255)
tim=turtle_module.Turtle()

tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list=[(252, 15, 192),(224, 17, 95),(255, 111, 255),(222, 111, 161),(255, 0, 144),(255, 102, 204),(251, 174, 210),(255, 105, 180),(255, 0, 255),(246, 74, 138),(222, 49, 99),(255, 166, 201),(251, 96, 127),(241, 156, 187),(249, 135, 197),(254, 91, 172),(248, 24, 148),(236, 85, 120),(253, 185, 200),(252, 163, 183)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots=100
for dot in range(1,number_of_dots+1):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)
    if dot%10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)




screen=turtle_module.Screen()
screen.exitonclick()
