


# def exam_mark(n):
#     if n>=90:
#         return "A"
#     elif 80<n<90:
#         return"B"
#     elif 70<=n<80:
#         return "C"
#     elif 60<= n <70 :
#         return "D"
#     else:
#         return "F"
# marks =[34,67,89,79,96]
# for mark in marks:
#     print("grade is",exam_mark(mark))
# mark=float(input("enter your mark:"))
# print("grade is" ,exam_mark(mark))


# import turtle
#
# def chooseColor(height):
#     if height >=200:
#         return "red"
#     elif height >= 100:
#         return "yellow"
#     else:
#         return "green"
# def drawBar(t, height, gap):
#     t.fillcolor(chooseColor(height))
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
#
#



# import turtle
#
# def chooseColor(height):
#     if height >=200:
#         return "red"
#     elif height >= 100:
#         return "yellow"
#     else:
#         return "green"
# def drawBar(t, height, gap):
#
#     t.fillcolor(chooseColor(height))
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
#     if height >= 0:
#         label_y = height + gap
#     else:
#         label_y = gap
#
#     t.forward(label_y)
#     t.write(height, align="center", font=("Arial", 12, "normal"))
#     t.backward(label_y)
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
# data = [48, -117, 200, -240, 160, 260, 220]
#
# barChart(data)
#
# turtle.done()
#
#









# import math
# def findHypot(lenght,height):
#     return math.sqrt(lenght**2 + height**2)
#
# print(findHypot(3,4))


def findHypot(lenght,height):
    return (lenght**2 + height**2)**0.5
print(findHypot(3,4))