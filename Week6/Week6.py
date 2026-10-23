# import turtle
#
# def drawPoly(someturtle, somesides, somesize):
#     for i in range(somesides):
#         someturtle.forward(somesize)
#         someturtle.left(360 / somesides)
#
# screen = turtle.Screen()
# screen.bgcolor("lightgreen")
#
# tess = turtle.Turtle()
# tess.color("hotpink")
# tess.pensize(3)
#
# drawPoly(tess, 8, 50)
#
# screen.exitonclick()



# import turtle
#
# def drawSquare(someturtle, somesize):
#     for i in range(4):
#         someturtle.forward(somesize)
#         someturtle.left(90)
#
# screen = turtle.Screen()
# screen.bgcolor("lightgreen")
#
# tess = turtle.Turtle()
# tess.color("blue")
# tess.speed(0)
#
# for i in range(20):
#     drawSquare(tess, 100)
#     tess.left(18)
#
# screen.exitonclick()




# import turtle
#
# def drawSpiral(someturtle, angle):
#     for i in range(100):
#         someturtle.forward(i * 2)
#         someturtle.right(angle)
#
# screen = turtle.Screen()
# screen.setup(900, 500)
# screen.bgcolor("lightgreen")
#
# tess = turtle.Turtle()
# tess.color("blue")
# tess.speed(0)
#
# tess.penup()
# tess.goto(-220, 0)
# tess.pendown()
#
# drawSpiral(tess, 90)
#
# tess.penup()
# tess.goto(220, 0)
# tess.setheading(0)
# tess.pendown()
#
# drawSpiral(tess, 89)
#
# screen.exitonclick()



# import turtle
#
# def drawPoly(someturtle, somesides, somesize):
#     for i in range(somesides):
#         someturtle.forward(somesize)
#         someturtle.left(360 / somesides)
#
# def drawEquitriangle(someturtle, somesize):
#     drawPoly(someturtle, 3, somesize)
#
# screen = turtle.Screen()
# screen.bgcolor("lightgreen")
#
# tess = turtle.Turtle()
# tess.color("hotpink")
# tess.pensize(3)
#
# drawEquitriangle(tess, 100)
#
# screen.exitonclick()



# import turtle
#
# def drawStar(someturtle, somesize):
#     for i in range(5):
#         someturtle.forward(somesize)
#         someturtle.right(144)
#
# screen = turtle.Screen()
# screen.setup(900, 700)
# screen.bgcolor("lightgreen")
#
# tess = turtle.Turtle()
# tess.color("hotpink")
# tess.speed(0)
#
# tess.penup()
# tess.goto(-250, 150)
# tess.pendown()
#
# for i in range(5):
#     drawStar(tess, 100)
#     tess.penup()
#     tess.forward(350)
#     tess.right(144)
#     tess.pendown()
#
# screen.exitonclick()




# import turtle
#
# def drawSprite(someturtle, legs, length):
#     for i in range(legs):
#         someturtle.forward(length)
#         someturtle.backward(length)
#         someturtle.left(360 / legs)
#
# screen = turtle.Screen()
# screen.bgcolor("lightgreen")
#
# tess = turtle.Turtle()
# tess.color("blue")
# tess.speed(0)
#
# drawSprite(tess, 15, 120)
#
# screen.exitonclick()