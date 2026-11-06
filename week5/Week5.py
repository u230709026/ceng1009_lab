# import random
# for i in range(10):
#     print(random.random())

# import random
# for i in range(10):
#     print(random.randint(25,35))

# import math
# hypotenuse= math.hypot(3,4)
# print(hypotenuse)

# import math
# def areaOfCircle(r):
#     return r*r*math.pi
# print (areaOfCircle(3))

# import turtle
# def drawStar(t,side) :
#     for i in range(5):
#         t.forward(side)
#         t.right(144)
#
# screen =turtle.Screen()
# tess = turtle.Turtle()
# tess.pensize(3)
#
# drawStar(tess,100)
# screen.exitonclick()

# import turtle
# alex = turtle.Turtle()
# alex.pensize(3)
# alex.pencolor("pink")
# screen = turtle.Screen()
# screen.bgcolor("green")
#
#
# for i in range(5):
#     alex.penup()
#     alex.forward(40)
#     for b in range(4):
#         alex.pendown()
#         alex.forward(20)
#         alex.left(90)
#
# screen.exitonclick()




# import turtle
# screen = turtle.Screen()
# screen.bgcolor("green")
# tess = turtle.Turtle()
# tess.pencolor("pink")
# tess.pensize(4)
# def drawSquare(t,side):
#     for i in range(4):
#         t.forward(side)
#         t.left(90)
#
# for i in range(20,120,20):
#   drawSquare(tess,i)
#   tess.penup()
#   tess.backward(10)
#   tess.right(90)
#   tess.forward(10)
#   tess.left(90)
#   tess.pendown()