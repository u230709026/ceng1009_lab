# def sumTo(n):
#     return (n * (n + 1)) // 2
#
# print(sumTo(10))
#





# import turtle
#
# def drawStar(t, n, size):
#     if n >= 3 and n % 2 == 1:
#         for i in range(n):
#             t.forward(size)
#             t.right(180 - 180 / n)
#     else:
#         print("n must be an odd number greater than or equal to 3.")
#
# screen = turtle.Screen()
# tess = turtle.Turtle()
#
# drawStar(tess, 7, 100)
#
# screen.exitonclick()



# def sumTo(n):
#     total = 0
#     for i in range(1,n+1):
#         total += i
#     return total
# print(sumTo(9))


# import math
#
# def mySqrt(x):
#
#     guess = x/2
#     for i in range(20):
#         guess =(1/2) * (guess + (x/guess))
#     return guess
# n = int(input("please enter a positive integer : "))
# print ("the result is " , mySqrt(n))
# print("the result is ",math.sqrt(n))


# import turtle
#
# def drawSprite(t, legs, length):
#     for i in range(legs):
#         t.forward(length)
#         t.backward(length)
#         t.left(360 / legs)
#
#
# def fancySquare(t, size):
#     for i in range(4):
#         drawSprite(t, 8, 25)
#         t.forward(size)
#         t.left(90)
#
# wn = turtle.Screen()
# tess = turtle.Turtle()
# tess.speed(6)
# tess.color("pink")
# tess.pensize(2)
#
# fancySquare(tess, 150)
#
# wn.exitonclick()
#



# import turtle
#
# def drawTriangle(t, size):
#     t.begin_fill()
#     for i in range(3):
#         t.forward(size)
#         t.left(120)
#     t.end_fill()
#
# def drawSpriteWithTriangle(t, legs, length):
#     for i in range(legs):
#         t.forward(length)
#         drawTriangle(t, 10)
#         t.backward(length)
#         t.left(360 / legs)
#
#
# def fancySquare(t, size):
#     for i in range(4):
#         drawSpriteWithTriangle(t, 8, 25)
#         t.forward(size)
#         t.left(90)
#
# wn = turtle.Screen()
# tess = turtle.Turtle()
# tess.speed(1)
# tess.color("lightgreen")
# tess.pensize(2)
# tess.fillcolor("lightgreen")
#
# fancySquare(tess, 150)
#
# wn.exitonclick()


# def checkSign(x):
#     if x > 0:
#         return "Positive"
#     elif x < 0:
#         return "Negative"
#     else:
#         return "Zero"
# numbers=[-7,6,0]
# for number in numbers:
#     print(number ,"is",checkSign(number))
#
#
# n = int(input("enter a number :"))
# print(checkSign(n))




# import turtle
#
# def drawBar(t, height, gap):
#     t.begin_fill()
#     t.left(90)
#     t.forward(height)
#     t.right(90)
#     t.forward(40)
#     t.right(90)
#     t.forward(height)
#     t.left(90)
#     t.end_fill()
#
#     t.penup()
#     t.backward(20)
#     t.left(90)
#     t.forward(height + gap)
#     t.write(height, align="center", font=("Arial", 12, "normal"))
#     t.backward(height + gap)
#     t.right(90)
#     t.forward(30)
#     t.pendown()
#
# def barChart(data):
#     if len(data) == 0:
#         return
#
#     maxheight = max(data)
#     border = max(10, maxheight * 0.1)
#     gap = (maxheight + border) * 0.05
#
#     screen = turtle.Screen()
#     screen.setworldcoordinates(
#         -border, -border,
#         len(data) * 50 + border,
#         maxheight + 2 * border
#     )
#
#     t = turtle.Turtle()
#     t.color("blue", "lightblue")
#     t.pensize(2)
#     t.speed(0)
#
#     for height in data:
#         drawBar(t, height, gap)
#
#     t.hideturtle()
#
# data = [48, 117, 200, 240, 160, 260, 220]
#
# barChart(data)
#
# turtle.done()






