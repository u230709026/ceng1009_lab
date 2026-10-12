for i in range(100):
    print("We like Python's turtles!")


for n in [12,10,32,3,66,17,42,99,20]:
    print(n)
for n in [12, 10, 32, 3, 66, 17, 42, 99, 20]:
    print(n,n*n )


import turtle
wn = turtle.Screen()
alex = turtle.Turtle()
bob = turtle.Turtle()
for a in range (3):
    alex.left(120)
    alex.forward(50)

for b in range(4):
    bob.left(90)
    bob.forward(50)
for b in range(6):
    bob.left(60)
    bob.forward(50)

for b in range(8):
    bob.left(45)
    bob.forward(50)



number_of_side = int(input("enter side number :"))
length_of_side = int (input("enter length of the size:"))
color = input("enter color:")
fill_color = input("enter fill color:")
import turtle
wn = turtle.Screen()
wn.bgcolor(fill_color)
alex = turtle.Turtle()
alex.color(color)
for n in range(number_of_side):
     alex.left(360/number_of_side)
     alex.forward(length_of_side)



import turtle
wn = turtle.Screen()
alex = turtle.Turtle()
for a in [160,-43, 270,-97,-43, 200,-940, 17,-86]:
    alex.left(a)
    alex.forward(100)



import turtle
wn = turtle.Screen()
alex = turtle.Turtle()
alex.left(54)
for n in range(5):
    alex.forward(100)
    alex.left(144)

wn.exitonclick()

import turtle
wn = turtle.Screen()
alex = turtle.Turtle()
alex.shape("turtle")
alex.penup()

for n in range(12):

    alex.forward(50)
    alex.stamp()
    alex.backward(50)
    alex.left(30)
wn.exitonclick()
legs = int(input("enter leg number:"))
import turtle
wn = turtle.Screen()
alex = turtle.Turtle()
for n in range(legs):
    alex.stamp()
    alex.forward(50)
    alex.backward(50)
    alex.left(360/legs)
wn.exitonclick()




